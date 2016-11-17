from django.db import models

from ...common.models.time import TimeStamp, DayTimeInterval
from ...common.models.schedule import PlaceEvent
from ...institution.schedule.models import AcademicSemester
from ...institution.facility.models import Place
from ...user.user.models import User
from ..course.models import Course


class CourseSession(TimeStamp):
    course = models.ForeignKey(Course)
    semester = models.ForeignKey(AcademicSemester)


class SessionInstructor(TimeStamp):
    session = models.ForeignKey(CourseSession)
    instructor = models.ForeignKey(User)


class SessionLesson(DayTimeInterval):
    course_session = models.ForeignKey(SessionInstructor)
    place = models.ForeignKey(Place)


class LessonEvent(PlaceEvent):
    course_session_lesson = models.ForeignKey(SessionLesson)
