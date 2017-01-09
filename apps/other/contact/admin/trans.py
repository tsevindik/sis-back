from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import trans


@admin.register(trans.CountryTrans)
class CountryTransAdmin(admin.ModelAdmin):
    pass


@admin.register(trans.CityTrans)
class CityTransAdmin(admin.ModelAdmin):
    pass


@admin.register(trans.RegionTrans)
class RegionTransAdmin(admin.ModelAdmin):
    pass


@admin.register(trans.LanguageTrans)
class LanguageTransAdmin(admin.ModelAdmin):
    pass
