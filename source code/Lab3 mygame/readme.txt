Balance Game Website Image 생성과정 

#####1. 데이터베이스 컨테이너 이미지 생성 
1) DB 초기화 스크립트인 init.sql 작성 
mkdir Dockerfile 
cd Dockerfile
mkdir -p mysql-init
vi mysql-init/init.sql

CREATE DATABASE IF NOT EXISTS balance_game_db;
USE balance_game_db;

CREATE TABLE IF NOT EXISTS games (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    votes_a INT DEFAULT 0,
    votes_b INT DEFAULT 0,
    image_url TEXT,
    is_closed BOOLEAN DEFAULT 0,
    start_date DATETIME
);

2) inti.sql실행이 포함된 컨테이너 실행 
docker run --name mygame-db \
    -e MYSQL_ALLOW_EMPTY_PASSWORD=yes \
    -e MYSQL_DATABASE=balance_game_db \
    -e MYSQL_USER=flaskuser \
    -e MYSQL_PASSWORD=1234 \
    -v $(pwd)/mysql-init:/docker-entrypoint-initdb.d \
    -p 3306:3306 \
    -d mysql:latest

3)DB 확인 후 현재 실행중인 컨테이너로 이미지 만들기
docker exec -it mygame-db mysql -u root
docker commit mygame-db <DockerHub Account>/mygame-db

4) 기존 컨테이너 정지/삭제 
docker stop mygame-db
docker rm mygame-db
docker rmi mysql

5) 새 이미지로 컨테이너 실행 
docker run --name mygame-db -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -e MYSQL_DATABASE=balance_game_db -e MYSQL_USER=flaskuser -e MYSQL_PASSWORD=1234 -v $(pwd)/mysql-init:/docker-entrypoint-initdb.d -p 3306:3306 -d <DockerHub Account>/mygame-db

6) 테이블 생성 확인
docker exec -it mygame-db mysql -u root

#####2. Application 컨테이너 이미지 생성 및 실행 
1) 컨테이너 이미지 생성 
cd Dockerfile
docker build -t <DockerHub Account>/mygame-app:1.0 .
2) 컨테이너 실행
docker run --name mygame-app -e MYSQL_HOST=mygame-db -e MYSQL_DATABASE=balance_game_db -e MYSQL_USER=flaskuser -e MYSQL_PASSWORD=1234 -p 8000:8000 --link mygame-db:mysql -d <DockerHub Account>/mygame-app:1.0


#####3. 접속테스트
공인IP/8000

#####4. DockerHub에 이미지 업로드 


