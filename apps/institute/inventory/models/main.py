from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models
from apps.institute.facility.models import BuildingRoom


class InventoryType(time_models.TimeStamp):
    pass


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
