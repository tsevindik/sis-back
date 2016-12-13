from django.utils.translation import ugettext_lazy as _
from django.db import models

from apps.other.contact.models import Language
from utils.models import time as time_models
from . import main


class CoursePoolTrans(time_models.TimeStamp):
    neutral = models.ForeignKey(
        main.CoursePool
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )
