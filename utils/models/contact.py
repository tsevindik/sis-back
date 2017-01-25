from cities.models import City
from django.utils.translation import ugettext_lazy as _
from django.db import models

from ..models.time import TimeStamp


class Address(TimeStamp):
    city = models.ForeignKey(
        City,
        verbose_name=_("Şehir")
    )
    district = models.CharField(
        max_length=50,
        verbose_name=_("İlçe")
    )
    postcode = models.IntegerField(
        verbose_name=_("Posta Kodu")
    )
    description = models.TextField(
        verbose_name=_("Açıklama")
    )

    class Meta:
        abstract = True


class Phone(TimeStamp):
    number = models.CharField(
        max_length=30,
        verbose_name=_("Numara")
    )

    class Meta:
        abstract = True
