from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.db import models

from ..models.time import TimeStamp


class Translation(TimeStamp):
    language_code = models.CharField(
        choices=settings.LANGUAGES,
        max_length=7,
        verbose_name=_("Dil")
    )

    class Meta:
        abstract = True
        unique_together = 'neutral', 'language_code'
        index_together = [["neutral", "language_code"]]

