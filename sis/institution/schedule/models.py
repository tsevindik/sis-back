from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...utils.time.models import DateInterval


class AcademicYear(DateInterval):
    title = models.CharField(
        max_length=50,
        verbose_name=_("Başlık")
    )


class AcademicSemester(DateInterval):
    title = models.CharField(
        max_length=80,
        verbose_name=_("Başlık")
    )
    academic_year = models.ForeignKey(AcademicYear)