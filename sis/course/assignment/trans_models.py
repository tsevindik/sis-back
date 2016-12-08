from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...main.contact.models import Language
from ...common.models.time import TimeStamp
from . import models as assignment_models


class AssignmentTypeTrans(TimeStamp):
    neutral = models.ForeignKey(
        assignment_models.AssignmentType
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )
