from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.time import TimeStamp
from ...common.models.contact import Address


class CampusAddress(Address):
    pass


class UniversityCampus(TimeStamp):
    name = models.CharField(
        max_length=150,
        verbose_name=_("İsim")
    )


class CampusPlace(TimeStamp):
    campus = models.ForeignKey(UniversityCampus)
    name = models.CharField(
        max_length=100,
        verbose_name=_("İsim"),
    )
    code = models.CharField(
        max_length=20,
        verbose_name=_("Kod")
    )
    floor = models.IntegerField(verbose_name=_("Kat"))
    capacity = models.IntegerField(verbose_name=_("Kapasite"))
