from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...institute.unit.models import UniversityUnit
from ...common.models.time import TimeStamp
from ...institute.institute.models import University


class UnitProgram(TimeStamp):
    name = models.CharField(
        max_length=150,
        verbose_name=_("İsim")
    )
    university_unit = models.ForeignKey(
        UniversityUnit,
        verbose_name=_("Üniversite Birimi")
    )
    is_multiple_degree = models.BooleanField(
        verbose_name=_("Çoklu Program")
    )
    description = models.TextField(
        verbose_name=_("Açıklama")
    )


class ProgramUniversity(TimeStamp):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )
    unit_program = models.ForeignKey(
        UnitProgram,
        verbose_name=_("Program")
    )
