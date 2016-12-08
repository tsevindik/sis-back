from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...main.contact.models import Language
from ...common.models.time import TimeStamp
from . import models as contact_models


class CountryTrans(TimeStamp):
    neutral = models.ForeignKey(
        contact_models.Country
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )


class CityTrans(TimeStamp):
    neutral = models.ForeignKey(
        contact_models.City
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )


class RegionTrans(TimeStamp):
    neutral = models.ForeignKey(
        contact_models.Region
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )


class LanguageTrans(TimeStamp):
    neutral = models.ForeignKey(
        contact_models.Language,
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
