from django.utils.translation import ugettext_lazy as _
from django.db import models

from .main import UnitProgram
from config.settings.common import AUTH_USER_MODEL
from utils.models import time as time_models


class ProgramAuth(time_models.TimeStamp):
    unit_program = models.ForeignKey(
        UnitProgram,
        verbose_name=_("Program")
    )
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("Kullanıcı")
    )
