from django.db import models

from ...common.models.schedule import Attendance
from ...user.user.models import User
from ..section.models import SessionEvent
from ..assignment.models import EventAssignmentSession


class StudentCourseAttendance(Attendance):
    event = models.ForeignKey(SessionEvent)
    student = models.ForeignKey(User)


class InstructorCourseAttendance(Attendance):
    event = models.ForeignKey(SessionEvent)
    instructor = models.ForeignKey(User)


class EventAssignmentAttendance(Attendance):
    session = models.ForeignKey(EventAssignmentSession)
    student = models.ForeignKey(User)
