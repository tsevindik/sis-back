from django.utils.translation import ugettext_lazy as _
from django.db import models

from . import main
from config.settings.common import AUTH_USER_MODEL
from utils.models import time as time_models


class ProgramAuth(time_models.TimeStamp):
    unit_program = models.ForeignKey(
        main.UnitProgram,
        verbose_name=_("Program")
    )
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("Kullanıcı")
    )
