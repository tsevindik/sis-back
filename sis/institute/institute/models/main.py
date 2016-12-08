from django.utils.translation import ugettext_lazy as _
from django.db import models

from ....main.contact.models import Language
from ....course.course.models import Course
from .common import AppTimeStamp


class University(AppTimeStamp):
    pass


class UniversityConfig(AppTimeStamp):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Üniversite")
    )


class UniversityCourse(AppTimeStamp):
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
