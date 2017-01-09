from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import main


@admin.register(main.MajorProgram)
class MajorProgramAdmin(admin.ModelAdmin):
    pass


@admin.register(main.MajorApplication)
class MajorApplicationAdmin(admin.ModelAdmin):
    pass
