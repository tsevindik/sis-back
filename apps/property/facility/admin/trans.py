from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import trans


@admin.register(trans.UniversityCampusTrans)
class UniversityCampusTransAdmin(admin.ModelAdmin):
    pass


@admin.register(trans.BuildingTypeTrans)
class BuildingTypeTransAdmin(admin.ModelAdmin):
    pass


@admin.register(trans.CampusBuildingTrans)
class CampusBuildingTransAdmin(admin.ModelAdmin):
    pass


@admin.register(trans.CampusBlockTrans)
class CampusBlockTransAdmin(admin.ModelAdmin):
    pass


@admin.register(trans.CampusBuildingTrans)
class RoomTypeTransAdmin(admin.ModelAdmin):
    pass


@admin.register(trans.CampusBlockTrans)
class BuildingRoomAdmin(admin.ModelAdmin):
    pass
