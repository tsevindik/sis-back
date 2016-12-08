from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...user.student.models import StudentProgram
from ...common.models.time import TimeStamp
from ...user.user.models import User
from ...common.models.user import UserProfile, UserAddress, UserPhone, INSTRUCTOR_WORK_STATUS, WORK_TIME


class InstructorProfile(UserProfile):
    work_status = models.CharField(
        max_length=1,
        choices=INSTRUCTOR_WORK_STATUS,
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


class InstructorPhone(UserPhone):
    pass


class InstructorAddress(UserAddress):
    pass


class ProgramAdviser(TimeStamp):
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )
    student_program = models.ForeignKey(
        StudentProgram,
        verbose_name=_("Öğrenci Programı")
    )
