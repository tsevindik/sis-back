from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import main


@admin.register(main.Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(main.City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(main.Region)
class RegionAdmin(admin.ModelAdmin):
    pass


@admin.register(main.Language)
class LanguageAdmin(admin.ModelAdmin):
    pass
