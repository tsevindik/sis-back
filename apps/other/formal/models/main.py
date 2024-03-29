from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models


class Certification(time_models.TimeStamp):
    name = models.CharField(
        max_length=150,
        verbose_name=_("İsim")
    )
    abbreviation = models.CharField(
        max_length=10,
        verbose_name=_("Kısaltma")
    )
    out_of_grade = models.IntegerField(
        verbose_name=_("Not Üzerinden")
    )
