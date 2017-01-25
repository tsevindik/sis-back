from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models
from apps.program.program.models import UnitProgram
from config.settings.common import AUTH_USER_MODEL


class MajorProgram(time_models.TimeStamp):
    unit_program = models.ForeignKey(
        UnitProgram,
        verbose_name=_("Program")
    )
    major_program = models.ForeignKey(
        UnitProgram,
        related_name="major_program",
        verbose_name=_("Anadal Programı")
    )


class MajorApplication(time_models.TimeStamp):
    major_program = models.ForeignKey(
        MajorProgram,
        verbose_name=_("Program")
    )
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("Kullanıcı")
    )
    is_approved = models.BooleanField(
        verbose_name=_("Onaylandı")
    )
