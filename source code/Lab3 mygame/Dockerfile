# 베이스 이미지로 Python 3.10 사용
FROM python:3.10

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 파일들을 복사
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY templates templates
COPY static static

# 필요한 패키지 설치
RUN pip install -r requirements.txt

# Flask 환경변수 설정
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000

# Flask 서버 실행
CMD ["flask", "run"]

