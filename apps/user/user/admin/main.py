from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import main


@admin.register(main.User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(main.UserUniversity)
class UserUniversityAdmin(admin.ModelAdmin):
    pass
