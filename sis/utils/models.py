from django.utils.translation import ugettext_lazy as _
from django.db import models

from .time.models import TimeStamp


class Type(TimeStamp):
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )

    class Meta:
        abstract = True
