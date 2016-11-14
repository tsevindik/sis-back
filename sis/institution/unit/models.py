from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...utils.time.models import TimeStamp
from ..models import University


class AcademicUnitType(TimeStamp):
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )


class AcademicUnit(TimeStamp):
    name = models.CharField(
        max_length=150,
        verbose_name=_("İsim")
    )
    university = models.ForeignKey(University)
    type = models.ForeignKey(AcademicUnitType)
    description = models.TextField(verbose_name=_("Açıklama"))


class AcademicProgram(TimeStamp):
    name = models.CharField(
        max_length=150,
        verbose_name=_("İsim")
    )
    description = models.TextField(verbose_name=_("Açıklama"))