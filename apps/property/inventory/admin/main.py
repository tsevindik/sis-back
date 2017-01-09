from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import main


@admin.register(main.InventoryType)
class InventoryTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(main.Inventory)
class InventoryAdmin(admin.ModelAdmin):
    pass


@admin.register(main.RoomInventory)
class RoomInventoryAdmin(admin.ModelAdmin):
    pass
