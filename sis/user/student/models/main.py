from django.utils.translation import ugettext_lazy as _
from django.db import models

from ....institute.program.models import UnitProgram
from ...user.models import User
from .common import AppTimeStamp, AppUserProfile, AppUserAddress, AppUserPhone


class StudentProfile(AppUserProfile):
    is_graduated = models.BooleanField(
        verbose_name=_("Mezun")
    )
    is_suspended = models.BooleanField(
        verbose_name=_("Kayıt Dondurdu")
    )
    is_quit = models.BooleanField(
        verbose_name=_("Ayrıldı")
    )


class StudentPhone(AppUserPhone):
    pass


class StudentAddress(AppUserAddress):
    pass


class StudentProgram(AppTimeStamp):
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )
    unit_program = models.ForeignKey(
        UnitProgram,
        verbose_name=_("Program")
    )
