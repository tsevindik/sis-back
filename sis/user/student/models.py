from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...institute.program.models import UnitProgram
from ...user.user.models import User
from ...common.models.time import TimeStamp
from ...common.models.user import UserProfile, UserPhone, UserAddress


class StudentProfile(UserProfile):
    is_graduated = models.BooleanField(
        verbose_name=_("Mezun")
    )
    is_suspended = models.BooleanField(
        verbose_name=_("Kayıt Dondurdu")
    )
    is_quit = models.BooleanField(
        verbose_name=_("Ayrıldı")
    )


class StudentPhone(UserPhone):
    pass


class StudentAddress(UserAddress):
    pass


class StudentProgram(TimeStamp):
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )
    unit_program = models.ForeignKey(
        UnitProgram,
        verbose_name=_("Program")
    )
