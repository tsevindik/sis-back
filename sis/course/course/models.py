from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.time import TimeStamp
from ...institute.institute.models import University
from ...institute.unit.models import UnitProgram, UniversityUnit


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


class UniversityCourse(TimeStamp):
    is_primary = models.BooleanField(
        verbose_name=_("Birincil")
    )
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )
    course = models.ForeignKey(
        Course,
        verbose_name=_("Ders")
    )


class UnitCourse(TimeStamp):
    course = models.ForeignKey(
        Course,
        verbose_name=_("Ders")
    )
    university_unit = models.ForeignKey(
        UniversityUnit,
        verbose_name=_("Üniversite Birimi")
    )


class ProgramCourse(TimeStamp):
    course = models.ForeignKey(
        Course,
        verbose_name=_("Ders")
    )
    unit_program = models.ForeignKey(
        UnitProgram,
        verbose_name=_("Program")
    )


class LetterGrade(TimeStamp):
    rank = models.IntegerField(
        verbose_name=_("Sıra")
    )
    name = models.CharField(
        max_length=3,
        verbose_name=_("İsim")
    )
    point = models.FloatField(
        verbose_name=_("Puan")
    )
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )
