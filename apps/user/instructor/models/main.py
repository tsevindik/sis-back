from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models
from apps.user.utils import models as user_models
from apps.user.student.models import StudentProgram
from apps.user.user.models import User
from apps.user.utils.models import WORK_TIME


WORK_STATUS = (
    (0, _('Kadrolu')),
    (1, _('Sözleşmeli')),
    (2, _('Ziyaretçi')),
    (2, _('İzinli')),
    (3, _('Ayrıldı'))
)


class InstructorProfile(user_models.UserProfile):
    work_status = models.CharField(
        max_length=1,
        choices=WORK_STATUS,
        verbose_name=_("Çalışma Durumu")
    )
    work_time = models.CharField(
        max_length=1,
        choices=WORK_TIME,
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
        User,
        verbose_name=_("Kullanıcı")
    )
    student_program = models.ForeignKey(
        StudentProgram,
        verbose_name=_("Öğrenci Programı")
    )
