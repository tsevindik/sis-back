from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.time import TimeStamp
from ..institute.models import University


class UnitType(TimeStamp):
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )
    university = models.ForeignKey(University)


class UniversityUnit(TimeStamp):
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
    unit = models.ForeignKey(UniversityUnit)
    is_multiple_degree = models.BooleanField()
    description = models.TextField(verbose_name=_("Açıklama"))


class ProgramUniversity(TimeStamp):
    university = models.ForeignKey(University)
    program = models.ForeignKey(UnitProgram)
