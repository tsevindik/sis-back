from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import trans as trans_models
from . import main


class EmployeeTransactionTypeTrans(trans_models.Translation):
    neutral = models.ForeignKey(
        main.EmployeeTransactionType
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_("İsim")
    )


class StudentTransactionTypeTrans(trans_models.Translation):
    neutral = models.ForeignKey(
        main.StudentTransactionType
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_("İsim")
    )
