from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.schedule import Attendance
from ...common.models.time import TimeStamp
from ...user.user.models import User
from ..session.models import Session, Event
from ..assignment.models import Assignment


class SessionEnrollment(TimeStamp):
    course_session = models.ForeignKey(Session)
    student = models.ForeignKey(User)


class StudentAttendance(Attendance):
    course_session_lesson_meeting = models.ForeignKey(Event)
    student = models.ForeignKey(User)


class Grade(TimeStamp):
    enrollment = models.ForeignKey(SessionEnrollment)
    assignment = models.ForeignKey(Assignment)
    grade = models.IntegerField(verbose_name=_("Not"))
