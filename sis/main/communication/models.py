from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...utils.time.models import TimeStamp
from ...utils.models import Type


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
    country = models.ForeignKey(Country)


class District(TimeStamp):
    city = models.ForeignKey(City)
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )


class AddressType(Type):
    pass


class Address(TimeStamp):
    type = models.ForeignKey(AddressType)
    district = models.ForeignKey(District)
    postcode = models.IntegerField(
        max_length=10,
        verbose_name=_("Posta Kodu")
    )
    description = models.TextField(verbose_name=_("Açıklama"))


class PhoneType(Type):
    pass


class Phone(TimeStamp):
    type = models.ForeignKey(PhoneType)
    number = models.CharField(
        max_length=30,
        verbose_name=_("Numara")
    )
