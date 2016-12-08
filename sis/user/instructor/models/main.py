from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...student.models import StudentProgram
from ...user.models import User
from ....common.models.user import WORK_TIME
from .common import AppTimeStamp, AppUserProfile, AppUserAddress, AppUserPhone


WORK_STATUS = (
    (0, _('Kadrolu')),
    (1, _('Sözleşmeli')),
    (2, _('Ziyaretçi')),
    (2, _('İzinli')),
    (3, _('Ayrıldı'))
)


class InstructorProfile(AppUserProfile):
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


class InstructorPhone(AppUserPhone):
    pass


class InstructorAddress(AppUserAddress):
    pass


class ProgramAdviser(AppTimeStamp):
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )
    student_program = models.ForeignKey(
        StudentProgram,
        verbose_name=_("Öğrenci Programı")
    )
