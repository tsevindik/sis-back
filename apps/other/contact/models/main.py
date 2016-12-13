from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models


class Country(time_models.TimeStamp):
    pass


class City(time_models.TimeStamp):
    country = models.ForeignKey(
        Country,
        verbose_name=_("Ülke")
    )


class Region(time_models.TimeStamp):
    city = models.ForeignKey(
        City,
        verbose_name=_("İl")
    )


class Language(time_models.TimeStamp):
    code = models.CharField(
        max_length=10,
        verbose_name=_("Kod")
    )
    country = models.ForeignKey(
        Country,
        verbose_name=_("Ülke")
    )
