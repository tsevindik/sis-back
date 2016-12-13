from django.utils.translation import ugettext_lazy as _
from django.db import models

from apps.other.contact import models as contact_models
from ..models.time import TimeStamp


class Address(TimeStamp):
    district = models.ForeignKey(
        contact_models.Region,
        null=True,
        blank=True,
        verbose_name=_("İlçe")
    )
    postcode = models.IntegerField(
        verbose_name=_("Posta Kodu")
    )

    class Meta:
        abstract = True


class AddressTrans(TimeStamp):
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
