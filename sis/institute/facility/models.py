from django.utils.translation import ugettext_lazy as _
from django.db import models

from ..institute.models import University
from ...common.models.time import TimeStamp
from ...common.models.contact import Address


class UniversityCampus(Address):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )
    has_blocks = models.BooleanField(
        verbose_name=_("Blok")
    )


class BuildingType(TimeStamp):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )


class CampusBuilding(Address):
    university_campus = models.ForeignKey(
        UniversityCampus,
        verbose_name=_("Kampüs")
    )
    type = models.ForeignKey(
        BuildingType,
        verbose_name=_("Bina Türü")
    )
    has_address = models.BooleanField(
        verbose_name=_("Adres")
    )


class CampusBlock(TimeStamp):
    university_campus = models.ForeignKey(
        UniversityCampus,
        verbose_name=_("Kampüs")
    )


class BlockBuilding(TimeStamp):
    campus_building = models.ForeignKey(
        CampusBuilding,
        verbose_name=_("Kampüs Binası")
    )
    campus_block = models.ForeignKey(
        CampusBlock,
        verbose_name=_("Kampüs Bloğu")
    )


class RoomType(TimeStamp):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )


class BuildingRoom(TimeStamp):
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
    campus_building = models.ForeignKey(
        CampusBuilding,
        verbose_name=_("Kampüs Binası")
    )
    type = models.ForeignKey(
        BuildingType,
        verbose_name=_("Bina Türü")
    )


# add translation models
from .trans_models import *
