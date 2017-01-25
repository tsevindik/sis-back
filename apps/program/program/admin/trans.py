from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import trans


@admin.register(trans.UnitProgramTrans)
class UnitProgramTransAdmin(admin.ModelAdmin):
    pass
