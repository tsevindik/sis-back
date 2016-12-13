from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models
from apps.institute.program.models import UnitProgram
from apps.user.user.models import User


class MajorProgram(time_models.TimeStamp):
    unit_program = models.ForeignKey(
        UnitProgram,
        verbose_name=_("Program")
    )
    major_program = models.ForeignKey(
        UnitProgram,
        verbose_name=_("Anadal Programı")
    )


class MinorProgram(time_models.TimeStamp):
    unit_program = models.ForeignKey(
        UnitProgram,
        verbose_name=_("Program")
    )
    minor_program = models.ForeignKey(
        UnitProgram,
        verbose_name=_("Yandal Programı")
    )


class MajorApplication(time_models.TimeStamp):
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


class MinorApplication(time_models.TimeStamp):
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
