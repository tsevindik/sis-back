from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...institute.institute.models import University
from ...common.models.time import DateInterval, TimeStamp


class Year(DateInterval):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )


class YearSemester(DateInterval):
    year = models.ForeignKey(
        Year,
        verbose_name=_("Yıl")
    )


class SemesterCalendar(TimeStamp):
    year_semester = models.ForeignKey(
        YearSemester,
        verbose_name=_("Dönem")
    )


class CalendarPeriod(DateInterval):
    semester_calendar = models.ForeignKey(
        SemesterCalendar,
        verbose_name=_("Takvim")
    )


# add translation models
from .trans_models import *
