from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import main


@admin.register(main.InstructorProfile)
class InstructorProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(main.InstructorPhone)
class InstructorPhoneAdmin(admin.ModelAdmin):
    pass


@admin.register(main.InstructorAddress)
class InstructorAddressAdmin(admin.ModelAdmin):
    pass


@admin.register(main.ProgramAdviser)
class ProgramAdviserAdmin(admin.ModelAdmin):
    pass
