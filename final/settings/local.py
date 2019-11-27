from .base import *
from decouple import config

SECRET_KEY = config('SECRET_KEY', default='e%gd@u_zpb3cb5u*o71j@jsv#d)+0=5+^iv8bif@rb$wpsvhib')

DEBUG = True

ALLOWED_HOSTS = []
