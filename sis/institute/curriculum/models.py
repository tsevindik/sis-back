from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.time import TimeStamp
from ...course.course.models import Course
from ...course.pool.models import CoursePool
from ...institute.program.models import ProgramSemester


class CurriculumCourse(TimeStamp):
    program_semester = models.ForeignKey(
        ProgramSemester,
        verbose_name=_("Dönem")
    )
    course = models.ForeignKey(
        Course,
        verbose_name=_("İsim")
    )


class CurriculumCoursePool(TimeStamp):
    program_semester = models.ForeignKey(
        ProgramSemester,

        verbose_name=_("Dönem")
    )
    course_pool = models.ForeignKey(
        CoursePool,
        verbose_name=_("Ders Havuzu")
    )
