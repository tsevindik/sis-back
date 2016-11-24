from django.db import models

from ...common.models.time import TimeStamp
from ..user.models import User


class StaffProfile(TimeStamp):
    staff = models.ForeignKey(User)
