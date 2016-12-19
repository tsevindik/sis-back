from django.utils.translation import ugettext_lazy as _
from django.db import models

from .main import UnitProgram
from apps.user.user.models import User
from utils.models import time as time_models


class ProgramAuth(time_models.TimeStamp):
    unit_program = models.ForeignKey(
        UnitProgram,
        verbose_name=_("Program")
    )
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )
