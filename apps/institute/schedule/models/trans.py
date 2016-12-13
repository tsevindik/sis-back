from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time
from apps.other.contact.models import Language
from . import main


class YearTrans(time.TimeStamp):
    neutral = models.ForeignKey(
        main.Year
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    title = models.CharField(
        max_length=50,
        verbose_name=_("Başlık")
    )


class YearSemesterTrans(time.TimeStamp):
    neutral = models.ForeignKey(
        main.YearSemester
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    title = models.CharField(
        max_length=80,
        verbose_name=_("Başlık")
    )


class SemesterCalendarTrans(time.TimeStamp):
    neutral = models.ForeignKey(
        main.SemesterCalendar
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    title = models.CharField(
        max_length=100,
        verbose_name=_("Başlık")
    )


class CalendarPeriodTrans(time.TimeStamp):
    neutral = models.ForeignKey(
        main.CalendarPeriod
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    title = models.CharField(
        max_length=300,
        verbose_name=_("Başlık")
    )
