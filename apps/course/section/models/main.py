from django.utils.translation import ugettext_lazy as _
from django.db import models

from apps.institute.schedule.models import YearSemester
from config.settings.common import AUTH_USER_MODEL
from apps.course.course.models import Course
from utils.models import time as time_models, schedule as schedule_models


class CourseSection(time_models.TimeStamp):
    course = models.ForeignKey(
        Course,
        verbose_name=_("Ders")
    )
    year_semester = models.ForeignKey(
        YearSemester,
        verbose_name=_("Dönem")
    )
    quota = models.IntegerField(
        verbose_name=_("Kontenjan")
    )
    implementation_type = models.CharField(
        max_length=1,
        choices=schedule_models.IMPLEMENTATION_TYPE,
        verbose_name=_("Uygulama Türü")
    )


class SectionInstructor(time_models.TimeStamp):
    course_section = models.ForeignKey(
        CourseSection,
        verbose_name=_("Ders Grubu")
    )
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("Kullanıcı")
    )


class SectionWeekSession(time_models.DayTimeInterval):
    course_section = models.ForeignKey(
        CourseSection,
        verbose_name=_("Ders Grubu")
    )


class SectionSession(schedule_models.CampusEvent):
    section_week_session = models.ForeignKey(
        SectionWeekSession,
        verbose_name=_("Haftalık Oturum")
    )
