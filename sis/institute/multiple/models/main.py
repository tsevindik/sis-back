from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...program.models import UnitProgram
from ....user.user.models import User
from .common import AppTimeStamp


class MajorProgram(AppTimeStamp):
    unit_program = models.ForeignKey(
        UnitProgram,
        verbose_name=_("Program")
    )
    major = models.ForeignKey(
        UnitProgram,
        verbose_name=_("Anadal")
    )


class MinorProgram(AppTimeStamp):
    unit_program = models.ForeignKey(
        UnitProgram,
        verbose_name=_("Program")
    )
    minor = models.ForeignKey(
        UnitProgram,
        verbose_name=_("Yandal")
    )


class MajorApplication(AppTimeStamp):
    major_program = models.ForeignKey(
        MajorProgram,
        verbose_name=_("Program")
    )
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )
    is_approved = models.BooleanField(
        verbose_name=_("Onaylandı")
    )


class MinorApplication(AppTimeStamp):
    minor_program = models.ForeignKey(
        MinorProgram,
        verbose_name=_("Program")
    )
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )
    is_approved = models.BooleanField(
        verbose_name=_("Onaylandı")
    )
