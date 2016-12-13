from django.utils.translation import ugettext_lazy as _
from django.db import models

from apps.institute.institute.models import University
from .utils import AppTimeStamp, AppDateInterval


class Year(AppDateInterval):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )


class YearSemester(AppDateInterval):
    year = models.ForeignKey(
        Year,
        verbose_name=_("Yıl")
    )


class SemesterCalendar(AppTimeStamp):
    year_semester = models.ForeignKey(
        YearSemester,
        verbose_name=_("Dönem")
    )


class CalendarPeriod(AppDateInterval):
    semester_calendar = models.ForeignKey(
        SemesterCalendar,
        verbose_name=_("Takvim")
    )
