from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...course.course.models import Course
from ...course.pool.models import CoursePool
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
    semester_number = models.IntegerField(
        verbose_name=_("Dönem Sayısı")
    )


class ProgramSemester(TimeStamp):
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )
    semester = models.IntegerField(
        verbose_name=_("Dönem")
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
