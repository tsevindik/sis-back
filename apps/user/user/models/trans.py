from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time
from apps.other.contact.models import Language
from . import main


class WorkStatusTrans(time.TimeStamp):
    neutral = models.ForeignKey(
        main.WorkStatus
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    title = models.CharField(
        max_length=50,
        verbose_name=_("Başlık")
    )
