from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models
from apps.other.contact.models import Language
from apps.course.course.models import Course


class University(time_models.TimeStamp):
    pass


class UniversityConfig(time_models.TimeStamp):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Üniversite")
    )


class UniversityCourse(time_models.TimeStamp):
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
