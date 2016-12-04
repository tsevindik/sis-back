from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.time import TimeStamp
from ...user.user.models import User
from ..section.models import CourseSection, SectionLetterGrade


class SectionRegistry(TimeStamp):
    course_section = models.ForeignKey(
        CourseSection,
        verbose_name=_("Ders Grubu")
    )
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )


class RegistryGrade(TimeStamp):
    section_registry = models.ForeignKey(
        SectionRegistry,
        verbose_name=_("Kayıt")
    )
    numeric_grade = models.FloatField(
        verbose_name=_("Sayısal Not")
    )
    letter_grade = models.ForeignKey(
        SectionLetterGrade,
        verbose_name=_("Harf Notu")
    )
    rank = models.IntegerField(
        verbose_name=_("Sıra")
    )
    percentile = models.FloatField(
        verbose_name=_("Yüzdelik Dilim")
    )
