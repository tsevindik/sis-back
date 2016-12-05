from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...user.student.models import StudentProgram
from ...common.models.time import TimeStamp
from ...user.user.models import User
from ...common.models.user import UserProfile, UserAddress, UserPhone


class InstructorProfile(UserProfile):
    pass


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
