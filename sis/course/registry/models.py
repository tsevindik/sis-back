from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.time import TimeStamp
from ...user.user.models import User
from ..session.models import CourseSession


class SessionRegistry(TimeStamp):
    session = models.ForeignKey(CourseSession)
    student = models.ForeignKey(User)

