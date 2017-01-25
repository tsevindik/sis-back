from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import trans


@admin.register(trans.UnitTypeTrans)
class UnitTypeTransAdmin(admin.ModelAdmin):
    pass


@admin.register(trans.UnitTrans)
class UnitTransAdmin(admin.ModelAdmin):
    pass
