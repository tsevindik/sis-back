from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...main.contact.models import Language
from ...course.course.models import Course
from ...common.models.time import TimeStamp


class University(TimeStamp):
    name = models.CharField(
        max_length=100,
        verbose_name=_("İsim")
    )


class UniversityConfig(TimeStamp):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Üniversite")
    )


class UniversityCourse(TimeStamp):
    is_primary = models.BooleanField(
        verbose_name=_("Birincil")
    )
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )
    course = models.ForeignKey(
        Course,
        verbose_name=_("Ders")
    )