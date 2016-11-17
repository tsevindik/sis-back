from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.time import TimeStamp
from ...institution.unit.models import AcademicProgram, AcademicUnit
from ...main.communication.models import Language


class Course(TimeStamp):
    academic_program = models.ForeignKey(
        AcademicProgram,
        null=True,
        blank=True
    )
    academic_unit = models.ForeignKey(
        AcademicUnit,
        null=True,
        blank=True
    )
    name = models.CharField(
        max_length=150,
        verbose_name=_("İsim")
    )
    description = models.TextField(
        verbose_name=_("Açıklama")
    )
    code = models.CharField(
        max_length=10,
        verbose_name=_("Kod")
    )
    theory = models.IntegerField(
        verbose_name=_("Teori")
    )
    practice = models.IntegerField(
        verbose_name=_("Pratik")
    )
    laboratory = models.IntegerField(
        verbose_name=_("Laboratuvar")
    )
    credit = models.IntegerField(
        verbose_name=_("Kredi")
    )
    ects = models.IntegerField(
        verbose_name=_("AKTS")
    )
    instruction_language = models.ForeignKey(Language)