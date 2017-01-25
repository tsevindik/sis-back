from .common import *

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default='0.0.0.0')
