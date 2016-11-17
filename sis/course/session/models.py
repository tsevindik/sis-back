from django.db import models

from ...common.models.time import TimeStamp, DayTimeInterval
from ...common.models.schedule import PlaceEvent
from ...institution.schedule.models import AcademicSemester
from ...institution.facility.models import Place
from ...user.user.models import User
from ..course.models import Course


class Session(TimeStamp):
    course = models.ForeignKey(Course)
    semester = models.ForeignKey(AcademicSemester)


class Instructor(TimeStamp):
    session = models.ForeignKey(Session)
    instructor = models.ForeignKey(User)


class Lesson(DayTimeInterval):
    course_session = models.ForeignKey(Session)
    place = models.ForeignKey(Place)


class Event(PlaceEvent):
    course_session_lesson = models.ForeignKey(Lesson)
