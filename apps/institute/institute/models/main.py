from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.db import models

from ..querysets import UniversityConfigQuerySet, UniversityQuerySet
from utils.models import time as time_models


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

    def save(self, *args, **kwargs):
        if self.is_primary and not self.id:
            raise Exception(_("Sadece bir tane birincil üniversite olabilir."))
        super(University, self).save(*args, **kwargs)

    class Meta:
        index_together = ["id", "is_primary"]


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

    def save(self, *args, **kwargs):
        if not self.id:
            raise Exception(_("Sadece bir tane üniversite seçenekleri olabilir."))
