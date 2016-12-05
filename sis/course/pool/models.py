from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...institute.unit.models import UniversityUnit
from ...common.models.time import TimeStamp
from ...course.course.models import Course
from ...institute.program.models import UnitProgram


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
    semester = models.IntegerField(
        verbose_name=_("Dönem")
    )
    unit_program = models.ForeignKey(
        UnitProgram,
        verbose_name=_("Program")
    )


class CoursePool(TimeStamp):
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )


class PoolCourse(TimeStamp):
    course_pool = models.ForeignKey(
        CoursePool,
        verbose_name=_("Ders Havuzu")
    )
    course = models.ForeignKey(
        Course,
        verbose_name=_("Ders")
    )
