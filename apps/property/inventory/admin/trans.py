from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import trans


@admin.register(trans.InventoryTypeTrans)
class InventoryTypeTransAdmin(admin.ModelAdmin):
    pass


@admin.register(trans.InventoryTrans)
class InventoryTransAdmin(admin.ModelAdmin):
    pass
