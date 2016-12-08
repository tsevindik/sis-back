from django.utils.translation import ugettext_lazy as _
from django.db import models

from ....main.contact.models import Language
from .common import AppTimeStamp
from . import main


class CoursePoolTrans(AppTimeStamp):
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