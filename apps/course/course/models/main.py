from django.utils.translation import ugettext_lazy as _
from django.db import models

from apps.institute.institute.models import University
from apps.institute.unit.models import Unit
from apps.program.program.models import UnitProgram
from utils.models import time as time_models


class Course(time_models.TimeStamp):
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
    by_secondary_university = models.BooleanField(
        verbose_name=_("İkincil Üniversiteye Tarafından")
    )


class CoursePrerequisite(time_models.TimeStamp):
    course = models.ForeignKey(
        Course,
        verbose_name=_("Ders")
    )
    prerequisite = models.ForeignKey(
        Course,
        related_name="prerequisite",
        verbose_name=_("Önkoşul Ders")
    )


class CourseCreditPrerequisite(time_models.TimeStamp):
    course = models.ForeignKey(
        Course,
        verbose_name=_("Ders")
    )
    prerequisite = models.IntegerField(
        verbose_name=_("Önkoşul Kredi")
    )


class UniversityCourse(time_models.TimeStamp):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )
    course = models.ForeignKey(
        Course,
        verbose_name=_("Ders")
    )


class UnitCourse(time_models.TimeStamp):
    course = models.ForeignKey(
        Course,
        verbose_name=_("Ders")
    )
    unit = models.ForeignKey(
        Unit,
        verbose_name=_("Birim")
    )


class ProgramCourse(time_models.TimeStamp):
    course = models.ForeignKey(
        Course,
        verbose_name=_("Ders")
    )
    unit_program = models.ForeignKey(
        UnitProgram,
        verbose_name=_("Program")
    )
