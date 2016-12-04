from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...institute.institute.models import University
from ...common.models.time import DateInterval, TimeStamp


class Year(DateInterval):
    title = models.CharField(
        max_length=50,
        verbose_name=_("Başlık")
    )
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )


class YearSemester(DateInterval):
    title = models.CharField(
        max_length=80,
        verbose_name=_("Başlık")
    )
    year = models.ForeignKey(
        Year,
        verbose_name=_("Yıl")
    )


class SemesterCalendar(TimeStamp):
    title = models.CharField(
        max_length=100,
        verbose_name=_("Başlık")
    )
    year_semester = models.ForeignKey(
        YearSemester,
        verbose_name=_("Dönem")
    )


class CalendarPeriod(DateInterval):
    title = models.CharField(
        max_length=200,
        verbose_name=_("Başlık")
    )
    semester_calendar = models.ForeignKey(
        SemesterCalendar,
        verbose_name=_("Takvim")
    )
