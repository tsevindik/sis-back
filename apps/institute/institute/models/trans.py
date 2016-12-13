from django.utils.translation import ugettext_lazy as _
from django.db import models

from ....other.contact.models import Language
from .utils import AppTimeStamp
from . import main


class UniversityTrans(AppTimeStamp):
    neutral = models.ForeignKey(
        main.University
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_("İsim")
    )
