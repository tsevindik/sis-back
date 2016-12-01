from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.time import TimeStamp
from ...institute.unit.models import UnitProgram, UniversityUnit
from ...main.contact.models import Language


class Course(TimeStamp):
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


class UnitCourse(TimeStamp):
    course = models.ForeignKey(Course)
    unit = models.ForeignKey(UniversityUnit)


class ProgramCourse(TimeStamp):
    course = models.ForeignKey(Course)
    program = models.ForeignKey(UnitProgram)


class LetterGrade(TimeStamp):
    rank = models.IntegerField(verbose_name=_("Sıra"))
    name = models.CharField(
        max_length=3,
        verbose_name=_("İsim")
    )
    point = models.FloatField(verbose_name=_("Puan"))
