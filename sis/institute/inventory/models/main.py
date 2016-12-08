from django.utils.translation import ugettext_lazy as _
from django.db import models

from ....institute.facility.models import BuildingRoom
from ....institute.institute.models import University
from .common import AppTimeStamp


class AssetType(AppTimeStamp):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )


class Asset(AppTimeStamp):
    type = models.ForeignKey(
        AssetType,
        verbose_name=_("Demirbaş Türü")
    )


class RoomInventory(AppTimeStamp):
    room = models.ForeignKey(
        BuildingRoom,
        verbose_name=_("Oda")
    )
    asset = models.ForeignKey(
        Asset,
        verbose_name=_("Mal")
    )
