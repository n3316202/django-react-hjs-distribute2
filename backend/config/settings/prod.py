# config/settings/dev.py
#개발 전용 설정만 덮어쓴다"는 의미
from .base import *  
import os #dev_4

DEBUG = False

#ALLOWED_HOSTS = ["example.com", "myapi.com"] 
#도메인에서 오는 요청만 Django가 처리
ALLOWED_HOSTS = ["*"]

# dev_4
# 정적파일 URL 경로
STATIC_URL = '/static/'
# collectstatic 명령어로 모이는 폴더 (EC2 내 정적파일 모음 경로)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# (개발 중에만) 추가 정적파일 경로 지정 가능
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]