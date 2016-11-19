from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.time import TimeStamp
from ...institute.unit.models import UnitProgram, Unit
from ...main.contact.models import Language


class Course(TimeStamp):
    unit = models.ForeignKey(
        Unit,
        null=True,
        blank=True
    )
    program = models.ForeignKey(
        UnitProgram,
        null=True,
        blank=True
    )
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
    instruction_language = models.ForeignKey(Language)
