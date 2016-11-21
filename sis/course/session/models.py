from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.time import TimeStamp, DayTimeInterval
from ...common.models.schedule import CampusEvent
from ...institute.schedule.models import YearSemester
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


class SessionLetterGrade(TimeStamp):
    session = models.ForeignKey(CourseSession)
    upper_number = models.FloatField(verbose_name=_("Üst Sınır (Sayı)"))
    lower_number = models.FloatField(verbose_name=_("Alt Sınır (Sayı)"))
    upper_percent = models.FloatField(verbose_name=_("Üst Sınır (Yüzde)"))
    lower_percent = models.FloatField(verbose_name=_("Alt Sınır (Yüzde)"))
    upper_rank = models.IntegerField(verbose_name=_("Üst Sınır (Sıra)"))
    lower_rank = models.IntegerField(verbose_name=_("Alt Sınır (Sıra)"))


class LessonEvent(CampusEvent):
    lesson = models.ForeignKey(SessionLesson)
