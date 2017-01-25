from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import main


@admin.register(main.Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(main.CoursePrerequisite)
class CoursePrerequisiteAdmin(admin.ModelAdmin):
    pass


@admin.register(main.CourseCreditPrerequisite)
class CourseCreditPrerequisiteAdmin(admin.ModelAdmin):
    pass
