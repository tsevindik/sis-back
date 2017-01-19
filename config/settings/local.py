from .common import *

DEBUG = os.getenv('DJANGO_DEBUG', True)

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', ['localhost', '127.0.0.1', '0.0.0.0'])
