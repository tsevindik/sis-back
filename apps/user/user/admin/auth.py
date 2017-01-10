from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import auth


@admin.register(auth.UserPermission)
class UserPermissionAdmin(admin.ModelAdmin):
    pass
