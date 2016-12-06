from django.utils.translation import ugettext_lazy as _
from django.db import models

from sis.course.assignment.models import SectionProcessAssignment
from ...main.registry.models import SectionRegistry
from ...course.section.models import CourseSection
from ...institute.institute.models import University
from ...common.models.time import TimeStamp


class LetterGrade(TimeStamp):
    rank = models.IntegerField(
        verbose_name=_("Sıra")
    )
    name = models.CharField(
        max_length=3,
        verbose_name=_("İsim")
    )
    point = models.FloatField(
        verbose_name=_("Puan")
    )
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
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


class AssignmentGrade(TimeStamp):
    section_registry = models.ForeignKey(
        SectionRegistry,
        verbose_name=_("Kayıt")
    )
    section_assignment = models.ForeignKey(
        SectionProcessAssignment,
        verbose_name=_("Grup Görevi")
    )
    grade = models.IntegerField(
        verbose_name=_("Not")
    )
