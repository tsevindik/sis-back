from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import trans as trans_models
from . import main


class AttendanceStatusTrans(trans_models.Translation):
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )

    class Meta:
        abstract = True


class StudentAttendanceStatusTrans(AttendanceStatusTrans):
    neutral = models.ForeignKey(
        main.StudentAttendanceStatus
    )


class InstructorAttendanceStatusTrans(AttendanceStatusTrans):
    neutral = models.ForeignKey(
        main.InstructorAttendanceStatus
    )
