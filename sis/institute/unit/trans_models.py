from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...main.contact.models import Language
from ...common.models.time import TimeStamp
from . import models as unit_models


class UnitTypeTrans(TimeStamp):
    neutral = models.ForeignKey(
        unit_models.UnitType
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )


class UniversityUnitTrans(TimeStamp):
    neutral = models.ForeignKey(
        unit_models.UniversityUnit
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=150,
        verbose_name=_("İsim")
    )
    description = models.TextField(
        verbose_name=_("Açıklama")
    )
