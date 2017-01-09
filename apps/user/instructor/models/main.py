from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models
from apps.user.utils import models as user_models
from apps.user.student.models import StudentProgram
from apps.user.user.models import WorkStatus
from config.settings.common import AUTH_USER_MODEL


class InstructorProfile(user_models.UserProfile):
    work_status = models.ForeignKey(
        WorkStatus,
        verbose_name=_("Çalışma Durumu")
    )
    work_time = models.CharField(
        max_length=1,
        choices=user_models.WORK_TIME,
        verbose_name=_("Çalışma Saati")
    )
    on_leave = models.BooleanField(
        verbose_name=_("İzinli")
    )
    is_quit = models.BooleanField(
        verbose_name=_("Ayrıldı")
    )


class InstructorPhone(user_models.UserPhone):
    pass


class InstructorAddress(user_models.UserAddress):
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
