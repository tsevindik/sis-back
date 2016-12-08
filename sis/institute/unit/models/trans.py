from django.utils.translation import ugettext_lazy as _
from django.db import models

from ....main.contact.models import Language
from .common import AppTimeStamp
from . import main


class UnitTypeTrans(AppTimeStamp):
    neutral = models.ForeignKey(
        main.UnitType
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )


class UniversityUnitTrans(AppTimeStamp):
    neutral = models.ForeignKey(
        main.UniversityUnit
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
