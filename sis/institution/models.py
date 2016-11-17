from django.utils.translation import ugettext_lazy as _
from django.db import models

from ..common.models.time import TimeStamp


class University(TimeStamp):
    name = models.CharField(max_length=100,
                            verbose_name=_("İsim"))
