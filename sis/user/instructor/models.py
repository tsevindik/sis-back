from django.db import models

from ...common.models.time import TimeStamp
from ..user.models import User


class InstructorProfile(TimeStamp):
    instructor = models.ForeignKey(User)
