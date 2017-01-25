from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import trans as trans_models
from . import main


class UniversityCampusTrans(trans_models.Translation):
    neutral = models.ForeignKey(
        main.Campus
    )
    name = models.CharField(
        max_length=150,
        verbose_name=_("İsim")
    )


class BuildingTypeTrans(trans_models.Translation):
    neutral = models.ForeignKey(
        main.BuildingType
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_("İsim")
    )


class CampusBuildingTrans(trans_models.Translation):
    neutral = models.ForeignKey(
        main.CampusBuilding
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_("İsim"),
    )


class CampusBlockTrans(trans_models.Translation):
    neutral = models.ForeignKey(
        main.CampusBlock
    )
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )


class RoomTypeTrans(trans_models.Translation):
    neutral = models.ForeignKey(
        main.RoomType
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_("İsim")
    )


class BuildingRoomTrans(trans_models.Translation):
    neutral = models.ForeignKey(
        main.BuildingRoom
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_("İsim")
    )
