from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import main


@admin.register(main.StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(main.StudentPhone)
class StudentPhoneAdmin(admin.ModelAdmin):
    pass


@admin.register(main.StudentAddress)
class StudentAddressAdmin(admin.ModelAdmin):
    pass


@admin.register(main.StudentProgram)
class StudentProgramAdmin(admin.ModelAdmin):
    pass
