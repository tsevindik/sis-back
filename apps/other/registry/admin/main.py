from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import main


@admin.register(main.SectionRegistry)
class SectionRegistryAdmin(admin.ModelAdmin):
    pass
