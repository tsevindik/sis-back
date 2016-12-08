from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.time import TimeStamp


class Country(TimeStamp):
    pass


class City(TimeStamp):
    country = models.ForeignKey(
        Country,
        verbose_name=_("Ülke")
    )


class Region(TimeStamp):
    city = models.ForeignKey(
        City,
        verbose_name=_("İl")
    )


class Language(TimeStamp):
    code = models.CharField(
        max_length=10,
        verbose_name=_("Kod")
    )
    country = models.ForeignKey(
        Country,
        verbose_name=_("Ülke")
    )


# add translation models
from .trans_models import *
