from django.contrib.postgres.fields import JSONField
from django.utils.translation import ugettext_lazy as _
from django.db import models

from apps.other.contact.models import Language
from utils.models import time as time_models
from apps.course.course.models import Course


class University(time_models.TimeStamp):
    """
    Attributes:
        data: university related neutral(untranslatable) data
            Sample JSON:
                {
                }
    """
    is_primary = models.BooleanField(
        default=False,
        verbose_name=_("Birincil")
    )
    data = JSONField(
        verbose_name=_("Veri")
    )


class UniversityConfig(time_models.TimeStamp):
    """
    Model for config of both system and university

    Attributes:
        language: default language of system
        data: university related neutral(untranslatable) data
            Sample JSON:
                {
                    major_count: number,    // Permitted number of major at a time
                    major_gpa: number,      // GPA needed to register second major
                    minor_count,            // Permitted number of minor at a time
                    minor_gpa: number,      // GPA needed to register second minor
                }
    """
    language = models.OneToOneField(
        Language,
        verbose_name=_("Üniversite")
    )
    data = JSONField(
        verbose_name=_("Veri")
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
