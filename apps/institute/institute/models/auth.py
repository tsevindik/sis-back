from django.utils.translation import ugettext_lazy as _
from django.db import models

from .main import University
from config.settings.common import AUTH_USER_MODEL
from utils.models import time as time_models


class UniversityAuth(time_models.TimeStamp):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("Kullanıcı")
    )
