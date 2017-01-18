from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import trans as trans_models
from ..querysets import UniversityTransQuerySet
from . import main


class UniversityTrans(trans_models.Translation):
    objects = UniversityTransQuerySet.as_manager()
    neutral = models.ForeignKey(
        main.University
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_("İsim")
    )
