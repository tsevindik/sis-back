from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import main


@admin.register(main.UnitProgram)
class UnitProgramAdmin(admin.ModelAdmin):
    pass


@admin.register(main.ProgramUniversity)
class ProgramUniversityAdmin(admin.ModelAdmin):
    pass


@admin.register(main.ProgramCourse)
class ProgramCourseAdmin(admin.ModelAdmin):
    pass
