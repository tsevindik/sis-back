from django.utils.translation import ugettext_lazy as _
from django.db import models

from apps.course.course.models import Course
from apps.course.pool.models import CoursePool
from apps.institute.program.models import ProgramSemester
from utils.models import time as time_models


class CurriculumCourse(time_models.TimeStamp):
    program_semester = models.ForeignKey(
        ProgramSemester,
        verbose_name=_("Dönem")
    )
    course = models.ForeignKey(
        Course,
        verbose_name=_("İsim")
    )


class CurriculumCoursePool(time_models.TimeStamp):
    program_semester = models.ForeignKey(
        ProgramSemester,
        verbose_name=_("Dönem")
    )
    course_pool = models.ForeignKey(
        CoursePool,
        verbose_name=_("Ders Havuzu")
    )
