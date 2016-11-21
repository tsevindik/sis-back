from django.db import models

from ...common.models.time import TimeStamp
from ..user.models import User


class StudentProfile(TimeStamp):
    student = models.ForeignKey(User)
