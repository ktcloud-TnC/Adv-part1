from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from datetime import datetime
import pytz
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL 설정 (환경 변수 사용)
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'mysql')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'flaskuser')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', '1234')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DATABASE', 'balance_game_db')

mysql = MySQL(app)

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM games WHERE is_closed = 0")
    games = cur.fetchall()
    cur.close()
    return render_template('index.html', games=games)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        question = request.form['question']
        option_a = request.form['option_a']
        option_b = request.form['option_b']
        file = request.files['image']
        filename = None
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        kst = pytz.timezone('Asia/Seoul')
        start_date = datetime.now(kst).strftime('%Y-%m-%d %H:%M:%S')

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO games (question, option_a, option_b, image_url, start_date) VALUES (%s, %s, %s, %s, %s)",
                    (question, option_a, option_b, filename, start_date))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('admin'))
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM games")
    games = cur.fetchall()
    cur.close()
    return render_template('admin.html', games=games)

@app.route('/close_game/<int:game_id>')
def close_game(game_id):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE games SET is_closed = 1 WHERE id = %s", (game_id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('admin'))

@app.route('/results/<int:game_id>')
def results(game_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM games WHERE id = %s", (game_id,))
    game = cur.fetchone()
    cur.close()
    return render_template('results.html', game=game)

@app.route('/vote', methods=['POST'])
def vote():
    game_id = request.form['game_id']
    option = request.form['option']
    cur = mysql.connection.cursor()
    if option == 'A':
        cur.execute("UPDATE games SET votes_a = votes_a + 1 WHERE id = %s", (game_id,))
    else:
        cur.execute("UPDATE games SET votes_b = votes_b + 1 WHERE id = %s", (game_id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('index'))

@app.route('/closed_games')
def closed_games():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM games WHERE is_closed = 1")
    games = cur.fetchall()
    cur.close()
    return render_template('closed_games.html', games=games)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

