from django.db import models
from django.contrib.auth.models import AbstractUser

from ...common.models.time import TimeStamp


class User(AbstractUser, TimeStamp):
    pass