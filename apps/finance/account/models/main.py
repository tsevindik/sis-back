from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models
from config.settings.common import AUTH_USER_MODEL


class EmployeeAccount(time_models.TimeStamp):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("Kullanıcı")
    )
    balance = models.FloatField(
        verbose_name=_("Bakiye")
    )


class StudentAccount(time_models.TimeStamp):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("Kullanıcı")
    )
    balance = models.FloatField(
        verbose_name=_("Bakiye")
    )
