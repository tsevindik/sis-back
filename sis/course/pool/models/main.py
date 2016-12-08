from django.utils.translation import ugettext_lazy as _
from django.db import models

from ....institute.unit.models import UniversityUnit
from ....institute.institute.models import University
from ....course.course.models import Course
from .common import AppTimeStamp


class CoursePool(AppTimeStamp):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )


class PoolUnit(AppTimeStamp):
    course_pool = models.ForeignKey(
        CoursePool,
        verbose_name=_("Ders")
    )
    unit = models.ForeignKey(
        UniversityUnit,
        verbose_name=_("Birim")
    )


class PoolCourse(AppTimeStamp):
    course_pool = models.ForeignKey(
        CoursePool,
        verbose_name=_("Ders Havuzu")
    )
    course = models.ForeignKey(
        Course,
        verbose_name=_("Ders")
    )
