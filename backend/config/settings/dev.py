# config/settings/dev.py
#개발 전용 설정만 덮어쓴다"는 의미
from .base import *  
import os
from pathlib import Path

# # 예시: 환경 변수 가져오기
# SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
# DEBUG = os.getenv("DJANGO_DEBUG", "False") == "True"
# ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "").split(",")


DEBUG = True

#ALLOWED_HOSTS = ["example.com", "myapi.com"] 
#도메인에서 오는 요청만 Django가 처리
ALLOWED_HOSTS = ["*"]

#dev_11 개발시 Origin 허용 - 배포시 불필요 - Nginx 프록시 이용시 
CORS_ORIGIN_ALLOW_ALL = True 