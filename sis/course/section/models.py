from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.schedule import IMPLEMENTATION_TYPE
from ...common.models.time import TimeStamp, DayTimeInterval
from ...common.models.schedule import CampusEvent
from ...institute.schedule.models import YearSemester
from ...user.user.models import User
from ..course.models import Course, LetterGrade


class CourseSection(TimeStamp):
    course = models.ForeignKey(Course)
    semester = models.ForeignKey(YearSemester)
    implementation = models.CharField(
        max_length=1,
        choices=IMPLEMENTATION_TYPE,
        verbose_name=_("Uygulama Türü")
    )


class SectionInstructor(TimeStamp):
    section = models.ForeignKey(CourseSection)
    instructor = models.ForeignKey(User)


class SectionSession(DayTimeInterval):
    section = models.ForeignKey(CourseSection)


class SectionLetterGrade(TimeStamp):
    section = models.ForeignKey(CourseSection)
    letter_grade = models.ForeignKey(LetterGrade)
    upper_number = models.FloatField(verbose_name=_("Üst Sınır (Sayı)"))
    lower_number = models.FloatField(verbose_name=_("Alt Sınır (Sayı)"))
    upper_percent = models.FloatField(verbose_name=_("Üst Sınır (Yüzde)"))
    lower_percent = models.FloatField(verbose_name=_("Alt Sınır (Yüzde)"))
    upper_rank = models.IntegerField(verbose_name=_("Üst Sınır (Sıra)"))
    lower_rank = models.IntegerField(verbose_name=_("Alt Sınır (Sıra)"))


class SessionEvent(CampusEvent):
    session = models.ForeignKey(SectionSession)
