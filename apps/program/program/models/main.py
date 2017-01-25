from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models
from apps.institute.unit.models import Unit
from apps.institute.institute.models import University


class UnitProgram(time_models.TimeStamp):
    unit = models.ForeignKey(
        Unit,
        verbose_name=_("Birim")
    )
    is_multiple_degree = models.BooleanField(
        verbose_name=_("Çoklu Program")
    )
    code = models.CharField(
        max_length=20,
        verbose_name=_("Kod")
    )
    semester_count = models.IntegerField(
        verbose_name=_("Dönem Sayısı")
    )


class ProgramUniversity(time_models.TimeStamp):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )
    unit_program = models.ForeignKey(
        UnitProgram,
        verbose_name=_("Program")
    )
