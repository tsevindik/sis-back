from django.utils.translation import ugettext_lazy as _
from django.db import models

from apps.other.contact.models import Language
from ..models.utils import AppTimeStamp
from . import main


class AssignmentTypeTrans(AppTimeStamp):
    neutral = models.ForeignKey(
        main.AssignmentType
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )
