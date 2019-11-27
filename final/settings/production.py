from .base import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['ssafy-jomajo.ymy57v3p2g.ap-northeast-2.elasticbeanstalk.com']
