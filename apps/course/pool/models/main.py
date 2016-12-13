from django.utils.translation import ugettext_lazy as _
from django.db import models

from apps.institute.unit.models import UniversityUnit
from apps.institute.institute.models import University
from apps.course.course.models import Course
from utils.models import time as time_models


class CoursePool(time_models.TimeStamp):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )


class PoolUnit(time_models.TimeStamp):
    course_pool = models.ForeignKey(
        CoursePool,
        verbose_name=_("Ders")
    )
    unit = models.ForeignKey(
        UniversityUnit,
        verbose_name=_("Birim")
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
