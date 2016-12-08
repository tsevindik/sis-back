from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...main.contact.models import Language
from ...common.models.time import TimeStamp
from . import models as schedule_models


class YearTrans(TimeStamp):
    neutral = models.ForeignKey(
        schedule_models.Year
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    title = models.CharField(
        max_length=50,
        verbose_name=_("Başlık")
    )


class YearSemesterTrans(TimeStamp):
    neutral = models.ForeignKey(
        schedule_models.YearSemester
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    title = models.CharField(
        max_length=80,
        verbose_name=_("Başlık")
    )


class SemesterCalendarTrans(TimeStamp):
    neutral = models.ForeignKey(
        schedule_models.SemesterCalendar
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    title = models.CharField(
        max_length=100,
        verbose_name=_("Başlık")
    )


class CalendarPeriodTrans(TimeStamp):
    neutral = models.ForeignKey(
        schedule_models.CalendarPeriod
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    title = models.CharField(
        max_length=300,
        verbose_name=_("Başlık")
    )
