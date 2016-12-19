from django.utils.translation import ugettext_lazy as _
from django.db import models

from .main import Unit
from apps.user.user.models import User
from utils.models import time as time_models


class UnitAuth(time_models.TimeStamp):
    unit = models.ForeignKey(
        Unit,
        verbose_name=_("Birim")
    )
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )
