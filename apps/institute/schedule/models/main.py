from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models
from apps.institute.institute.models import University


class Year(time_models.DateInterval):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )


class YearSemester(time_models.DateInterval):
    year = models.ForeignKey(
        Year,
        verbose_name=_("Yıl")
    )


class SemesterCalendar(time_models.TimeStamp):
    year_semester = models.ForeignKey(
        YearSemester,
        verbose_name=_("Dönem")
    )


class CalendarPeriod(time_models.DateInterval):
    semester_calendar = models.ForeignKey(
        SemesterCalendar,
        verbose_name=_("Takvim")
    )
