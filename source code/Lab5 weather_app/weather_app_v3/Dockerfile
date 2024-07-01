# 기본 이미지 설정
FROM python:3.8-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 설치
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . .

# 컨테이너 시작 시 실행할 명령어 설정
CMD ["python", "app.py"]

