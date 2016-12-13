from django.utils.translation import ugettext_lazy as _
from django.db import models

from .utils import AppTimeStamp


class Country(AppTimeStamp):
    pass


class City(AppTimeStamp):
    country = models.ForeignKey(
        Country,
        verbose_name=_("Ülke")
    )


class Region(AppTimeStamp):
    city = models.ForeignKey(
        City,
        verbose_name=_("İl")
    )


class Language(AppTimeStamp):
    code = models.CharField(
        max_length=10,
        verbose_name=_("Kod")
    )
    country = models.ForeignKey(
        Country,
        verbose_name=_("Ülke")
    )
