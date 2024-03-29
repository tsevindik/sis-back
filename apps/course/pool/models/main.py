from django.utils.translation import ugettext_lazy as _
from django.db import models

from apps.institute.unit.models import Unit
from apps.course.course.models import Course
from apps.program.program.models import UnitProgram
from utils.models import time as time_models


class CoursePool(time_models.TimeStamp):
    pass


class PoolUnit(time_models.TimeStamp):
    course_pool = models.ForeignKey(
        CoursePool,
        verbose_name=_("Ders")
    )
    unit = models.ForeignKey(
        Unit,
        verbose_name=_("Birim")
    )


class PoolProgram(time_models.TimeStamp):
    course_pool = models.ForeignKey(
        CoursePool,
        verbose_name=_("Ders")
    )
    unit_program = models.ForeignKey(
        UnitProgram,
        verbose_name=_("Program")
    )


class PoolCourse(time_models.TimeStamp):
    course_pool = models.ForeignKey(
        CoursePool,
        verbose_name=_("Ders Havuzu")
    )
    course = models.ForeignKey(
        Course,
        verbose_name=_("Ders")
    )
