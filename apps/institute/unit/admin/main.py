from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import main


@admin.register(main.UnitType)
class UnitTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(main.Unit)
class UnitAdmin(admin.ModelAdmin):
    pass


@admin.register(main.UnitCourse)
class UnitCourseAdmin(admin.ModelAdmin):
    pass


@admin.register(main.UnitBuilding)
class UnitBuildingAdmin(admin.ModelAdmin):
    pass
