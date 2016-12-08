from django.utils.translation import ugettext_lazy as _
from django.db import models

from .main import Language
from .common import AppTimeStamp
from . import main


class CountryTrans(AppTimeStamp):
    neutral = models.ForeignKey(
        main.Country
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )


class CityTrans(AppTimeStamp):
    neutral = models.ForeignKey(
        main.City
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )


class RegionTrans(AppTimeStamp):
    neutral = models.ForeignKey(
        main.Region
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )


class LanguageTrans(AppTimeStamp):
    neutral = models.ForeignKey(
        main.Language,
        related_name="neutral_language"
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )
