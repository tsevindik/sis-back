from django.utils.translation import ugettext_lazy as _
from django.db import models

from .time import TimeStamp


class BoolStatus(TimeStamp):
    status = models.BooleanField(
        verbose_name=_("Durum")
    )

    class Meta:
        abstract = True
