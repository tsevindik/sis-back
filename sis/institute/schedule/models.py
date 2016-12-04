from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...institute.institute.models import University
from ...common.models.time import DateInterval


class Year(DateInterval):
    title = models.CharField(
        max_length=50,
        verbose_name=_("Başlık")
    )
    university = models.ForeignKey(University)


class YearSemester(DateInterval):
    title = models.CharField(
        max_length=80,
        verbose_name=_("Başlık")
    )
    academic_year = models.ForeignKey(Year)


class SemesterCalendar(DateInterval):
    title = models.CharField(
        max_length=100,
        verbose_name=_("Başlık")
    )
    semester = models.ForeignKey(YearSemester)


class CalendarPeriod(DateInterval):
    title = models.CharField(
        max_length=200,
        verbose_name=_("Başlık")
    )
    calendar = models.ForeignKey(SemesterCalendar)
