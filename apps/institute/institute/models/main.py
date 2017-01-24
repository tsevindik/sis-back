from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.db import models

from ..querysets import UniversityConfigQuerySet, UniversityQuerySet
from utils.models import time as time_models


class University(time_models.TimeStamp):
    objects = UniversityQuerySet.as_manager()
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
    primary_university = models.OneToOneField(
        University,
        verbose_name=_("Birincil Üniversite")
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

    def save(self, *args, **kwargs):
        if not self.id:
            raise Exception(_("Sadece bir tane üniversite seçenekleri olabilir."))
