from django.utils.translation import ugettext_lazy as _
from django.db import models

from .main import Unit
from config.settings.common import AUTH_USER_MODEL
from utils.models import time as time_models


class UnitAuth(time_models.TimeStamp):
    unit = models.ForeignKey(
        Unit,
        verbose_name=_("Birim")
    )
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("Kullanıcı")
    )
