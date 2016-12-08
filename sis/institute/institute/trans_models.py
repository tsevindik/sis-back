from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...main.contact.models import Language
from ...common.models.time import TimeStamp
from . import models as institute_models


class UniversityTrans(TimeStamp):
    neutral = models.ForeignKey(
        institute_models.University
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_("İsim")
    )
