from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import main


@admin.register(main.Campus)
class CampusAdmin(admin.ModelAdmin):
    pass


@admin.register(main.BuildingType)
class BuildingTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(main.CampusBuilding)
class CampusBuildingAdmin(admin.ModelAdmin):
    pass


@admin.register(main.CampusBlock)
class CampusBlockAdmin(admin.ModelAdmin):
    pass


@admin.register(main.BlockBuilding)
class BlockBuildingAdmin(admin.ModelAdmin):
    pass


@admin.register(main.RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(main.BuildingRoom)
class BuildingRoomAdmin(admin.ModelAdmin):
    pass
