from django.db import models

from ...common.models.schedule import Attendance
from ...user.user.models import User
from ..section.models import LessonEvent
from ..assignment.models import EventAssignmentSession


class StudentLessonAttendance(Attendance):
    event = models.ForeignKey(LessonEvent)
    student = models.ForeignKey(User)


class InstructorLessonAttendance(Attendance):
    event = models.ForeignKey(LessonEvent)
    instructor = models.ForeignKey(User)


class EventAssignmentAttendance(Attendance):
    session = models.ForeignKey(EventAssignmentSession)
    student = models.ForeignKey(User)
