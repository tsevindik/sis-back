from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time, contact
from apps.other.contact.models import Language
from . import main


class UniversityCampusTrans(contact.AddressTrans):
    neutral = models.ForeignKey(
        main.UniversityCampus
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=150,
        verbose_name=_("İsim")
    )


class BuildingTypeTrans(time.TimeStamp):
    neutral = models.ForeignKey(
        main.BuildingType
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_("İsim")
    )


class CampusBuildingTrans(contact.AddressTrans):
    neutral = models.ForeignKey(
        main.CampusBuilding
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_("İsim"),
    )


class CampusBlockTrans(time.TimeStamp):
    neutral = models.ForeignKey(
        main.CampusBlock
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )


class RoomTypeTrans(time.TimeStamp):
    neutral = models.ForeignKey(
        main.RoomType
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_("İsim")
    )


class BuildingRoomTrans(time.TimeStamp):
    neutral = models.ForeignKey(
        main.BuildingRoom
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_("İsim")
    )
