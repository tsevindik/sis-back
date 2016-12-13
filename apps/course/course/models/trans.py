from django.utils.translation import ugettext_lazy as _
from django.db import models

from ....other.contact.models import Language
from .utils import AppTimeStamp
from . import main


class CourseTrans(AppTimeStamp):
    neutral = models.ForeignKey(
        main.Course
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=150,
        verbose_name=_("İsim")
    )
    description = models.TextField(
        verbose_name=_("Açıklama")
    )
