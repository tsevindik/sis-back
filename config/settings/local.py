from .common import *

DEBUG = env.bool('DJANGO_DEBUG', default=True)

ALLOWED_LOCAL_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

ALLOWED_HOSTS = ALLOWED_LOCAL_HOSTS + env.list('DJANGO_ALLOWED_HOSTS', default='0.0.0.0')
