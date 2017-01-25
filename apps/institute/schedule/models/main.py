from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models


class Year(time_models.DateInterval):
    pass


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
