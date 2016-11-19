from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.time import DateInterval
from ...common.models.schedule import Event


class Year(DateInterval):
    title = models.CharField(
        max_length=50,
        verbose_name=_("Başlık")
    )


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


class CalendarEvent(Event):
    calendar = models.ForeignKey(SemesterCalendar)
