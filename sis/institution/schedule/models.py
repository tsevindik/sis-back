from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...utils.time.models import DateTimeInterval


class Event(DateTimeInterval):
    title = models.CharField(verbose_name=_("Başlık"))

    class Meta:
        abstract = True
