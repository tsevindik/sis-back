from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import auth


@admin.register(auth.UniversityAuth)
class UniversityAuthAdmin(admin.ModelAdmin):
    pass
