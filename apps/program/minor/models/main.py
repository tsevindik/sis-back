from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models
from apps.program.program.models import UnitProgram
from config.settings.common import AUTH_USER_MODEL


class MinorProgram(time_models.TimeStamp):
    unit_program = models.ForeignKey(
        UnitProgram,
        verbose_name=_("Program")
    )
    minor_program = models.ForeignKey(
        UnitProgram,
        related_name="minor_program",
        verbose_name=_("Yandal Programı")
    )


class MinorApplication(time_models.TimeStamp):
    minor_program = models.ForeignKey(
        MinorProgram,
        verbose_name=_("Program")
    )
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("Kullanıcı")
    )
    is_approved = models.BooleanField(
        verbose_name=_("Onaylandı")
    )
