from django.utils.translation import ugettext_lazy as _
from django.db import models

from apps.institute.program.models import UnitProgram
from apps.user.user.models import User
from .utils import AppTimeStamp


class MajorProgram(AppTimeStamp):
    unit_program = models.ForeignKey(
        UnitProgram,
        verbose_name=_("Program")
    )
    major_program = models.ForeignKey(
        UnitProgram,
        verbose_name=_("Anadal Programı")
    )


class MinorProgram(AppTimeStamp):
    unit_program = models.ForeignKey(
        UnitProgram,
        verbose_name=_("Program")
    )
    minor_program = models.ForeignKey(
        UnitProgram,
        verbose_name=_("Yandal Programı")
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
