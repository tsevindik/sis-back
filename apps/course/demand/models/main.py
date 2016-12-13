from django.utils.translation import ugettext_lazy as _
from django.db import models

from apps.course.course.models import Course
from apps.course.section.models import CourseSection
from apps.user.user.models import User
from utils.models import time as time_models


class StudentQuotaDemand(time_models.TimeStamp):
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )
    course_section = models.ForeignKey(
        CourseSection,
        verbose_name=_("Ders Grubu")
    )


class StudentCourseDemand(time_models.TimeStamp):
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )
    course = models.ForeignKey(
        Course,
        verbose_name=_("Ders")
    )
    semester = models.IntegerField(
        verbose_name=_("Dönem")
    )


class InstructorCourseDemand(time_models.TimeStamp):
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )
    course = models.ForeignKey(
        Course,
        verbose_name=_("Ders")
    )
    semester = models.IntegerField(
        verbose_name=_("Dönem")
    )
