from django.utils.translation import ugettext_lazy as _
from django.db import models

from apps.program.program.models import UnitProgram
from apps.institute.unit.models import Unit
from utils.models import time as time_models


class ProgramTuitionFee(time_models.TimeStamp):
    unit_program = models.ForeignKey(
        UnitProgram,
        verbose_name=_("Program")
    )
    fee = models.PositiveIntegerField(
        verbose_name=_("Ücret")
    )


class ProgramCreditFee(time_models.TimeStamp):
    unit = models.ForeignKey(
        Unit,
        verbose_name=_("Birim")
    )
    fee = models.PositiveIntegerField(
        verbose_name=_("Ücret")
    )
