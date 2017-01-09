from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import trans


@admin.register(trans.WorkStatusTrans)
class WorkStatusTransAdmin(admin.ModelAdmin):
    pass
