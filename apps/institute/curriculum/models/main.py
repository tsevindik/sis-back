from django.utils.translation import ugettext_lazy as _
from django.db import models

from apps.course.course.models import Course
from apps.course.pool.models import CoursePool
from apps.institute.program.models import ProgramSemester
from .utils import AppTimeStamp


class CurriculumCourse(AppTimeStamp):
    program_semester = models.ForeignKey(
        ProgramSemester,
        verbose_name=_("Dönem")
    )
    course = models.ForeignKey(
        Course,
        verbose_name=_("İsim")
    )


class CurriculumCoursePool(AppTimeStamp):
    program_semester = models.ForeignKey(
        ProgramSemester,
        verbose_name=_("Dönem")
    )
    course_pool = models.ForeignKey(
        CoursePool,
        verbose_name=_("Ders Havuzu")
    )
