from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.schedule import IMPLEMENTATION_TYPE
from ...common.models.time import TimeStamp, DayTimeInterval
from ...common.models.schedule import CampusEvent
from ...institute.schedule.models import YearSemester
from ...user.user.models import User
from ..course.models import Course, LetterGrade


class CourseSection(TimeStamp):
    course = models.ForeignKey(
        Course,
        verbose_name=_("Ders")
    )
    year_semester = models.ForeignKey(
        YearSemester,
        verbose_name=_("Dönem")
    )
    implementation_type = models.CharField(
        max_length=1,
        choices=IMPLEMENTATION_TYPE,
        verbose_name=_("Uygulama Türü")
    )


class SectionInstructor(TimeStamp):
    course_section = models.ForeignKey(
        CourseSection,
        verbose_name=_("Ders Grubu")
    )
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )


class SectionSession(DayTimeInterval):  # todo: try to rename it
    course_section = models.ForeignKey(
        CourseSection,
        verbose_name=_("Ders Grubu")
    )


class SectionLetterGrade(TimeStamp):
    course_section = models.ForeignKey(
        CourseSection,
        verbose_name=_("Ders Grubu")
    )
    letter_grade = models.ForeignKey(
        LetterGrade,
        verbose_name=_("Harf Notu")
    )
    upper_number = models.FloatField(
        verbose_name=_("Üst Sınır (Sayı)")
    )
    lower_number = models.FloatField(
        verbose_name=_("Alt Sınır (Sayı)")
    )
    upper_percent = models.FloatField(
        verbose_name=_("Üst Sınır (Yüzde)")
    )
    lower_percent = models.FloatField(
        verbose_name=_("Alt Sınır (Yüzde)")
    )
    upper_rank = models.IntegerField(
        verbose_name=_("Üst Sınır (Sıra)")
    )
    lower_rank = models.IntegerField(
        verbose_name=_("Alt Sınır (Sıra)")
    )


class SessionEvent(CampusEvent):  # todo: try to rename it
    section_session = models.ForeignKey(
        SectionSession,
        verbose_name=_("Oturum")
    )
