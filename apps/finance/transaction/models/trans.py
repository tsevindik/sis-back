from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time
from apps.other.contact.models import Language
from . import main


class EmployeeTransactionTypeTrans(time.TimeStamp):
    neutral = models.ForeignKey(
        main.EmployeeTransactionType
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_("İsim")
    )


class StudentTransactionTypeTrans(time.TimeStamp):
    neutral = models.ForeignKey(
        main.StudentTransactionType
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_("İsim")
    )
