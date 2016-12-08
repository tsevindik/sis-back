from django.utils.translation import ugettext_lazy as _
from django.db import models

from ....course.course.models import Course
from ....institute.unit.models import UniversityUnit
from ....institute.institute.models import University
from .common import AppTimeStamp


class UnitProgram(AppTimeStamp):
    university_unit = models.ForeignKey(
        UniversityUnit,
        verbose_name=_("Üniversite Birimi")
    )
    is_multiple_degree = models.BooleanField(
        verbose_name=_("Çoklu Program")
    )


class ProgramUniversity(AppTimeStamp):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )
    unit_program = models.ForeignKey(
        UnitProgram,
        verbose_name=_("Program")
    )
    semester_count = models.IntegerField(
        verbose_name=_("Dönem Sayısı")
    )


class ProgramSemester(AppTimeStamp):
    semester = models.IntegerField(
        verbose_name=_("Dönem")
    )


class ProgramCourse(AppTimeStamp):
    course = models.ForeignKey(
        Course,
        verbose_name=_("Ders")
    )
    unit_program = models.ForeignKey(
        UnitProgram,
        verbose_name=_("Program")
    )
