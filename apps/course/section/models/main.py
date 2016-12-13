from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import schedule
from apps.institute.schedule.models import YearSemester
from apps.user.user.models import User
from apps.course.course.models import Course
from .utils import AppTimeStamp, AppDayTimeInterval, AppCampusEvent


class CourseSection(AppTimeStamp):
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
        choices=schedule.IMPLEMENTATION_TYPE,
        verbose_name=_("Uygulama Türü")
    )


class SectionInstructor(AppDayTimeInterval):
    course_section = models.ForeignKey(
        CourseSection,
        verbose_name=_("Ders Grubu")
    )
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )


class SectionWeekSession(AppDayTimeInterval):
    course_section = models.ForeignKey(
        CourseSection,
        verbose_name=_("Ders Grubu")
    )


class SectionSession(AppCampusEvent):
    section_week_session = models.ForeignKey(
        SectionWeekSession,
        verbose_name=_("Haftalık Oturum")
    )
