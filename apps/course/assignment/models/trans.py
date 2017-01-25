from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import trans as trans_models
from . import main


class AssignmentTypeTrans(trans_models.Translation):
    neutral = models.ForeignKey(
        main.AssignmentType
    )
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )
