from django.contrib.postgres.fields import JSONField
from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models
from apps.other.contact.models import Language
from . import main


class UniversityTrans(time_models.TimeStamp):
    """
    Attributes:
        neutral: actual model having neutral data
        language: language of translatable data
        data: all university related translatable data
            Sample JSON:
                {
                    name: string,
                }
    """
    neutral = models.ForeignKey(
        main.University
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    data = JSONField(
        verbose_name=_("Veri")
    )
