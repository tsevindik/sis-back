from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models, contact as contact_models
from apps.institute.institute.models import University


class UniversityCampus(contact_models.Address):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )
    has_blocks = models.BooleanField(
        verbose_name=_("Blok")
    )


class BuildingType(time_models.TimeStamp):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )


class CampusBuilding(contact_models.Address):
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


class CampusBlock(time_models.TimeStamp):
    university_campus = models.ForeignKey(
        UniversityCampus,
        verbose_name=_("Kampüs")
    )


class BlockBuilding(time_models.TimeStamp):
    campus_building = models.ForeignKey(
        CampusBuilding,
        verbose_name=_("Kampüs Binası")
    )
    campus_block = models.ForeignKey(
        CampusBlock,
        verbose_name=_("Kampüs Bloğu")
    )


class RoomType(time_models.TimeStamp):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )


class BuildingRoom(time_models.TimeStamp):
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
