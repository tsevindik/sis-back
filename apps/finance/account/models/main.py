from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models
from apps.user.user.models import User


class EmployeeAccount(time_models.TimeStamp):
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )
    balance = models.FloatField(
        verbose_name=_("Bakiye")
    )


class StudentAccount(time_models.TimeStamp):
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )
    balance = models.FloatField(
        verbose_name=_("Bakiye")
    )
