from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import main


@admin.register(main.MinorProgram)
class MinorProgramAdmin(admin.ModelAdmin):
    pass


@admin.register(main.MinorApplication)
class MinorApplicationAdmin(admin.ModelAdmin):
    pass
