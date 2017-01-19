from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.db import models

from ..querysets import UniversityConfigQuerySet, UniversityQuerySet
from utils.models import time as time_models
from apps.course.course.models import Course


class University(time_models.TimeStamp):
    objects = UniversityQuerySet.as_manager()
    is_primary = models.BooleanField(
        help_text=_("Sistemin yöneticisi Üniversite"),
        verbose_name=_("Birincil Üniversite")
    )
    official_name = models.CharField(
        max_length=100,
        verbose_name=_("Resmi İsim")
    )


class UniversityConfig(time_models.TimeStamp):
    objects = UniversityConfigQuerySet.as_manager()
    default_language = models.CharField(
        choices=settings.LANGUAGES,
        max_length=7,
        verbose_name=_("Dil")
    )
    major_count = models.IntegerField(
        verbose_name=_("Anadal Sayısı")
    )
    major_gpa = models.FloatField(
        verbose_name=_("Anadal Ortalama Sınırı")
    )
    minor_count = models.IntegerField(
        verbose_name=_("Yandal Sayısı")
    )
    minor_gpa = models.FloatField(
        verbose_name=_("Yandal Ortalama Sınırı")
    )


class UniversityCourse(time_models.TimeStamp):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )
    course = models.ForeignKey(
        Course,
        verbose_name=_("Ders")
    )
