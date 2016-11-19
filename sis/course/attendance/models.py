from django.db import models

from ...common.models.schedule import Attendance
from ...user.user.models import User
from ..session.models import LessonEvent


class StudentLessonAttendance(Attendance):
    event = models.ForeignKey(LessonEvent)
    student = models.ForeignKey(User)
