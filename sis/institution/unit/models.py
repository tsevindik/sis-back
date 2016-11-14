from django.utils.translation import ugettext_lazy as _
from django.db import models

from ..models import University


class AcademicUnitType(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )


class AcademicUnit(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name=_("İsim")
    )
    university = models.ForeignKey(University)
    type = models.ForeignKey(AcademicUnitType)
    description = models.TextField(verbose_name=_("Açıklama"))
