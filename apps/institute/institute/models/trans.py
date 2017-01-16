from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings

from utils.models import trans as trans_models
from . import main


class UniversityTrans(trans_models.Translation):
    neutral = models.ForeignKey(
        main.University
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_("İsim")
    )