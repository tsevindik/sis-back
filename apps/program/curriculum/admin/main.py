from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import main


@admin.register(main.CurriculumCourse)
class CurriculumCourseAdmin(admin.ModelAdmin):
    pass


@admin.register(main.CurriculumCoursePool)
class CurriculumCoursePoolAdmin(admin.ModelAdmin):
    pass
