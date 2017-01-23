from django.utils.translation import ugettext_lazy as _
from django.db import models

from apps.course.course.models import Course
from apps.course.section.models import CourseSection
from apps.institute.schedule.models import YearSemester
from config.settings.common import AUTH_USER_MODEL
from utils.models import time as time_models


class StudentQuotaDemand(time_models.TimeStamp):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("Kullanıcı")
    )
    course_section = models.ForeignKey(
        CourseSection,
        verbose_name=_("Ders Grubu")
    )


class CourseDemand(time_models.TimeStamp):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("Kullanıcı")
    )
    course = models.ForeignKey(
        Course,
        verbose_name=_("Ders")
    )
    year_semester = models.ForeignKey(
        YearSemester,
        verbose_name=_("Dönem")
    )

    class Meta:
        abstract = True


class StudentCourseDemand(CourseDemand):
    pass


class InstructorCourseDemand(CourseDemand):
    pass
