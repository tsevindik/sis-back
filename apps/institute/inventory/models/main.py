from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models
from apps.institute.facility.models import BuildingRoom
from apps.institute.institute.models import University


class InventoryType(time_models.TimeStamp):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )


class Inventory(time_models.TimeStamp):
    inventory_type = models.ForeignKey(
        InventoryType,
        verbose_name=_("Demirbaş Türü")
    )


class RoomInventory(time_models.TimeStamp):
    room = models.ForeignKey(
        BuildingRoom,
        verbose_name=_("Oda")
    )
    inventory = models.ForeignKey(
        Inventory,
        verbose_name=_("Demirbaş")
    )
    count = models.PositiveIntegerField(
        verbose_name=_("Sayı")
    )
