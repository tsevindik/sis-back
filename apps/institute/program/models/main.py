from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models
from apps.course.course.models import Course
from apps.institute.unit.models import UniversityUnit
from apps.institute.institute.models import University


class UnitProgram(time_models.TimeStamp):
    university_unit = models.ForeignKey(
        UniversityUnit,
        verbose_name=_("Üniversite Birimi")
    )
    is_multiple_degree = models.BooleanField(
        verbose_name=_("Çoklu Program")
    )


class ProgramUniversity(time_models.TimeStamp):
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


class ProgramSemester(time_models.TimeStamp):
    semester = models.IntegerField(
        verbose_name=_("Dönem")
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
