from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.time import TimeStamp


class Country(TimeStamp):
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )


class City(TimeStamp):
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )
    country = models.ForeignKey(
        Country,
        verbose_name=_("Ülke")
    )


class District(TimeStamp):
    city = models.ForeignKey(
        City,
        verbose_name=_("İl")
    )
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )


class Language(TimeStamp):
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )
    country = models.ForeignKey(
        Country,
        verbose_name=_("Ülke")
    )
