from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models
from apps.institute.facility.models import BuildingRoom
from apps.institute.institute.models import University


class AssetType(time_models.TimeStamp):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )


class Asset(time_models.TimeStamp):
    type = models.ForeignKey(
        AssetType,
        verbose_name=_("Demirbaş Türü")
    )


class RoomInventory(time_models.TimeStamp):
    room = models.ForeignKey(
        BuildingRoom,
        verbose_name=_("Oda")
    )
    asset = models.ForeignKey(
        Asset,
        verbose_name=_("Mal")
    )
