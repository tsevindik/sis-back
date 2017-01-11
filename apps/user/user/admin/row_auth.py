from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import row_auth


@admin.register(row_auth.UniversityAuth)
class UniversityAuthAdmin(admin.ModelAdmin):
    pass


@admin.register(row_auth.UnitAuth)
class UnitAuthAdmin(admin.ModelAdmin):
    pass


@admin.register(row_auth.ProgramAuth)
class ProgramAuthAdmin(admin.ModelAdmin):
    pass


@admin.register(row_auth.CourseAuth)
class CourseAuthAdmin(admin.ModelAdmin):
    pass


@admin.register(row_auth.SectionAuth)
class SectionAuthAdmin(admin.ModelAdmin):
    pass
