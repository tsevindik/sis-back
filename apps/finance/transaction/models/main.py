from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models
from config.settings.common import AUTH_USER_MODEL


class EmployeeTransactionType(time_models.TimeStamp):
    pass


class EmployeeTransaction(time_models.TimeStamp):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("Kullanıcı")
    )
    employee_action_type = models.ForeignKey(
        EmployeeTransactionType,
        verbose_name=_("İşlem Türü")
    )
    transaction_amount = models.FloatField(
        verbose_name=_("İşlem Tutarı")
    )


class StudentTransactionType(time_models.TimeStamp):
    pass


class StudentTransaction(time_models.TimeStamp):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("Kullanıcı")
    )
    student_action_type = models.ForeignKey(
        StudentTransactionType,
        verbose_name=_("İşlem Türü")
    )
    transaction_amount = models.FloatField(
        verbose_name=_("İşlem Tutarı")
    )
