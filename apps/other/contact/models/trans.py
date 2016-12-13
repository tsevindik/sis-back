from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models
from .main import Language
from . import main


class CountryTrans(time_models.TimeStamp):
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


class CityTrans(time_models.TimeStamp):
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


class RegionTrans(time_models.TimeStamp):
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


class LanguageTrans(time_models.TimeStamp):
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
