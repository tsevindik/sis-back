from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import main


@admin.register(main.University)
class UniversityAdmin(admin.ModelAdmin):
    pass


@admin.register(main.UniversityConfig)
class UniversityConfigAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
