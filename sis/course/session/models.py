from django.db import models

from ...common.models.time import TimeStamp, DayTimeInterval
from ...common.models.schedule import CampusPlaceEvent
from ...institute.schedule.models import YearSemester
from ...institute.facility.models import CampusPlace
from ...user.user.models import User
from ..course.models import Course


class CourseSession(TimeStamp):
    course = models.ForeignKey(Course)
    semester = models.ForeignKey(YearSemester)


class SessionInstructor(TimeStamp):
    session = models.ForeignKey(CourseSession)
    instructor = models.ForeignKey(User)


class SessionLesson(DayTimeInterval):
    session = models.ForeignKey(CourseSession)
    place = models.ForeignKey(CampusPlace)


class LessonEvent(CampusPlaceEvent):
    lesson = models.ForeignKey(SessionLesson)
