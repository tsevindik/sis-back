from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.time import TimeStamp
from ...course.course.models import Course


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
