from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...main.contact.models import District
from ..models.time import TimeStamp


class Address(TimeStamp):
    district = models.ForeignKey(
        District,
        null=True,
        blank=True,
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
