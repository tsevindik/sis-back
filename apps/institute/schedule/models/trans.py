from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import trans as trans_models
from . import main


class YearTrans(trans_models.Translation):
    neutral = models.ForeignKey(
        main.Year
    )
    title = models.CharField(
        max_length=50,
        verbose_name=_("Başlık")
    )


class YearSemesterTrans(trans_models.Translation):
    neutral = models.ForeignKey(
        main.YearSemester
    )
    title = models.CharField(
        max_length=80,
        verbose_name=_("Başlık")
    )


class SemesterCalendarTrans(trans_models.Translation):
    neutral = models.ForeignKey(
        main.SemesterCalendar
    )
    title = models.CharField(
        max_length=100,
        verbose_name=_("Başlık")
    )


class CalendarPeriodTrans(trans_models.Translation):
    neutral = models.ForeignKey(
        main.CalendarPeriod
    )
    title = models.CharField(
        max_length=300,
        verbose_name=_("Başlık")
    )
