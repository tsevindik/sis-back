from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import main


@admin.register(main.StaffProfile)
class StaffProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(main.StaffPhone)
class StaffPhoneAdmin(admin.ModelAdmin):
    pass


@admin.register(main.StaffAddress)
class StaffAddressAdmin(admin.ModelAdmin):
    pass
