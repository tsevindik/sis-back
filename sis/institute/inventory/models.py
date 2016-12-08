from django.utils.translation import ugettext_lazy as _
from django.db import models

from sis.institute.facility.models import BuildingRoom
from ...institute.institute.models import University
from ...common.models.time import TimeStamp


class AssetType(TimeStamp):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )


class Asset(TimeStamp):
    type = models.ForeignKey(
        AssetType,
        verbose_name=_("Demirbaş Türü")
    )


class RoomInventory(TimeStamp):
    room = models.ForeignKey(
        BuildingRoom,
        verbose_name=_("Oda")
    )
    asset = models.ForeignKey(
        Asset,
        verbose_name=_("Mal")
    )


# add translation models
from .trans_models import *
