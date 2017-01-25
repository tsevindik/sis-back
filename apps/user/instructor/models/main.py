from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...user.models import UserAddress, UserPhone
from ...worker.models import WorkStatus, WorkerProfile
from utils.models import time as time_models
from apps.user.student.models import StudentProgram
from config.settings.common import AUTH_USER_MODEL


class InstructorProfile(WorkerProfile):
    work_status = models.ManyToManyField(
        WorkStatus
    )


class InstructorPhone(UserPhone):
    pass


class InstructorAddress(UserAddress):
    pass


class ProgramAdviser(time_models.TimeStamp):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("Kullanıcı")
    )
    student_program = models.ForeignKey(
        StudentProgram,
        verbose_name=_("Öğrenci Programı")
    )
