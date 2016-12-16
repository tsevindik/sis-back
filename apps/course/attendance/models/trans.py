from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models
from apps.other.contact.models import Language
from . import main


class StudentAttendanceStatusTrans(time_models.TimeStamp):
    neutral = models.ForeignKey(
        main.StudentAttendanceStatus
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )


class InstructorAttendanceStatusTrans(time_models.TimeStamp):
    neutral = models.ForeignKey(
        main.InstructorAttendanceStatus
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )

