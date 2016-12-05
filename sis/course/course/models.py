from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.time import TimeStamp


class Course(TimeStamp):
    name = models.CharField(
        max_length=150,
        verbose_name=_("İsim")
    )
    description = models.TextField(
        verbose_name=_("Açıklama")
    )
    code = models.CharField(
        max_length=10,
        verbose_name=_("Kod")
    )
    theory = models.IntegerField(
        verbose_name=_("Teori")
    )
    practice = models.IntegerField(
        verbose_name=_("Pratik")
    )
    laboratory = models.IntegerField(
        verbose_name=_("Laboratuvar")
    )
    credit = models.IntegerField(
        verbose_name=_("Kredi")
    )
    ects = models.IntegerField(
        verbose_name=_("AKTS")
    )


class CoursePrerequisite(TimeStamp):
    course = models.ForeignKey(
        Course,
        verbose_name=_("Ders")
    )
    prerequisite = models.ForeignKey(
        Course,
        related_name="prerequisite",
        verbose_name=_("Önkoşul Ders")
    )


class CourseCreditPrerequisite(TimeStamp):
    course = models.ForeignKey(
        Course,
        verbose_name=_("Ders")
    )
    prerequisite = models.IntegerField(
        verbose_name=_("Önkoşul Kredi")
    )
