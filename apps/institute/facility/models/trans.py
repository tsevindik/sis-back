from django.utils.translation import ugettext_lazy as _
from django.db import models

from apps.other.contact.models import Language
from .utils import AppTimeStamp, AppAddressTrans
from . import main


class UniversityCampusTrans(AppAddressTrans):
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


class BuildingTypeTrans(AppTimeStamp):
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


class CampusBuildingTrans(AppAddressTrans):
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


class CampusBlockTrans(AppTimeStamp):
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


class RoomTypeTrans(AppTimeStamp):
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


class BuildingRoomTrans(AppTimeStamp):
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
