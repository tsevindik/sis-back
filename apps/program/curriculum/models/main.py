from django.utils.translation import ugettext_lazy as _
from django.db import models

from apps.course.course.models import Course
from apps.course.pool.models import CoursePool
from apps.program.program.models import UnitProgram
from utils.models import time as time_models


class Curriculum(time_models.TimeStamp):
    unit_program = models.ForeignKey(
        UnitProgram,
        verbose_name=_("Program")
    )
    program_semester = models.IntegerField(
        verbose_name=_("Program Dönemi")
    )


class CurriculumCourse(Curriculum):
    course = models.ForeignKey(
        Course,
        verbose_name=_("İsim")
    )


class CurriculumCoursePool(Curriculum):
    course_pool = models.ForeignKey(
        CoursePool,
        verbose_name=_("Ders Havuzu")
    )
