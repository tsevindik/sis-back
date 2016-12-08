from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.contact import AddressTrans
from ...main.contact.models import Language
from ...common.models.time import TimeStamp
from . import models as facility_models


class UniversityCampusTrans(AddressTrans):
    neutral = models.ForeignKey(
        facility_models.UniversityCampus
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=150,
        verbose_name=_("İsim")
    )


class BuildingTypeTrans(TimeStamp):
    neutral = models.ForeignKey(
        facility_models.BuildingType
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_("İsim")
    )


class CampusBuildingTrans(AddressTrans):
    neutral = models.ForeignKey(
        facility_models.CampusBuilding
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_("İsim"),
    )


class CampusBlockTrans(TimeStamp):
    neutral = models.ForeignKey(
        facility_models.CampusBlock
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )


class RoomTypeTrans(TimeStamp):
    neutral = models.ForeignKey(
        facility_models.RoomType
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_("İsim")
    )


class BuildingRoomTrans(TimeStamp):
    neutral = models.ForeignKey(
        facility_models.BuildingRoom
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_("İsim")
    )
