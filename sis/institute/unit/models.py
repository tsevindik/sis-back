from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.time import TimeStamp
from ..institute.models import University


class UnitType(TimeStamp):
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )


class Unit(TimeStamp):
    name = models.CharField(
        max_length=150,
        verbose_name=_("İsim")
    )
    university = models.ForeignKey(University)
    type = models.ForeignKey(UnitType)
    description = models.TextField(verbose_name=_("Açıklama"))


class UnitProgram(TimeStamp):
    name = models.CharField(
        max_length=150,
        verbose_name=_("İsim")
    )
    description = models.TextField(verbose_name=_("Açıklama"))