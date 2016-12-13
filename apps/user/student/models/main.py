from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models
from apps.user.utils import models as user_models
from apps.institute.program.models import UnitProgram
from apps.user.user.models import User


class StudentProfile(user_models.UserProfile):
    is_graduated = models.BooleanField(
        verbose_name=_("Mezun")
    )
    is_suspended = models.BooleanField(
        verbose_name=_("Kayıt Dondurdu")
    )
    is_quit = models.BooleanField(
        verbose_name=_("Ayrıldı")
    )


class StudentPhone(user_models.UserPhone):
    pass


class StudentAddress(user_models.UserAddress):
    pass


class StudentProgram(time_models.TimeStamp):
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )
    unit_program = models.ForeignKey(
        UnitProgram,
        verbose_name=_("Program")
    )
