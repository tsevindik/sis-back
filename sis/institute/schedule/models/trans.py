from django.utils.translation import ugettext_lazy as _
from django.db import models

from ....main.contact.models import Language
from .common import AppTimeStamp
from . import main


class YearTrans(AppTimeStamp):
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


class YearSemesterTrans(AppTimeStamp):
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


class SemesterCalendarTrans(AppTimeStamp):
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


class CalendarPeriodTrans(AppTimeStamp):
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
