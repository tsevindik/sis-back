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
    name = models.CharField(
        max_length=150,
        verbose_name=_("İsim")
    )


class CampusBuilding(Address):
    name = models.CharField(
        max_length=100,
        verbose_name=_("İsim"),
    )
    university_campus = models.ForeignKey(
        UniversityCampus,
        verbose_name=_("Kampüs")
    )
    has_blocks = models.BooleanField(
        verbose_name=_("Blok")
    )


class BuildingBlock(TimeStamp):
    name = models.CharField(
        max_length=100,
        verbose_name=_("İsim"),
    )
    campus_building = models.ForeignKey(
        CampusBuilding,
        verbose_name=_("Kampüs Binası")
    )


class BuildingRoom(TimeStamp):
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
    campus_building = models.ForeignKey(
        CampusBuilding,
        verbose_name=_("Kampüs Binası")
    )


class BlockRoom(TimeStamp):
    building_block = models.ForeignKey(
        BuildingBlock,
        verbose_name=_("Blok")
    )
    building_room = models.ForeignKey(
        BuildingRoom,
        verbose_name=_("Oda")
    )
