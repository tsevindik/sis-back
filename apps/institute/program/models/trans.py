from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time
from apps.other.contact.models import Language
from . import main


class UnitProgramTrans(time.TimeStamp):
    neutral = models.ForeignKey(
        main.UnitProgram
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=150,
        verbose_name=_("İsim")
    )
    description = models.TextField(
        verbose_name=_("Açıklama")
    )


class ProgramSemesterTrans(time.TimeStamp):
    neutral = models.ForeignKey(
        main.ProgramSemester
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )
