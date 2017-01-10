from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models
from . import main


class UserPermission(time_models.TimeStamp):
    user = models.OneToOneField(
        main.User,
        verbose_name=_("Kullanıcı")
    )
    university = models.BooleanField(
        verbose_name=_("Üniversite")
    )
    all_universities = models.BooleanField(
        verbose_name=_("Ders")
    )
    unit = models.BooleanField(
        verbose_name=_("Ders")
    )
    all_units = models.BooleanField(
        verbose_name=_("Ders")
    )
    program = models.BooleanField(
        verbose_name=_("Ders")
    )
    all_programs = models.BooleanField(
        verbose_name=_("Ders")
    )
    course = models.BooleanField(
        verbose_name=_("Ders")
    )
    all_courses = models.BooleanField(
        verbose_name=_("Bütün Dersler")
    )
    section = models.BooleanField(
        verbose_name=_("Ders")
    )
    all_sections = models.BooleanField(
        verbose_name=_("Ders")
    )
