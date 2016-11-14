from django.utils.translation import ugettext_lazy as _
from django.db import models

from ..time.models import DateTimeInterval


class Event(DateTimeInterval):
    title = models.CharField(
        max_length=200,
        verbose_name=_("Başlık")
    )

    class Meta:
        abstract = True
