from django.utils.translation import ugettext_lazy as _
from django.db import models

from ..institute.models import University
from ...common.models.time import TimeStamp
from ...common.models.contact import Address


class CampusAddress(Address):
    pass


class UniversityCampus(TimeStamp):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )
    name = models.CharField(
        max_length=150,
        verbose_name=_("İsim")
    )
    campus_address = models.ForeignKey(
        CampusAddress,
        verbose_name=_("Kampüs Adresi")
    )


class CampusPlace(TimeStamp):
    university_campus = models.ForeignKey(
        UniversityCampus,
        verbose_name=_("Kampüs")
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_("İsim"),
    )
    code = models.CharField(
        max_length=20,
        verbose_name=_("Kod")
    )
    floor = models.IntegerField(
        verbose_name=_("Kat")
    )
    capacity = models.IntegerField(
        verbose_name=_("Kapasite")
    )
