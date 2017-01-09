from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import main


@admin.register(main.CoursePool)
class CoursePoolAdmin(admin.ModelAdmin):
    pass


@admin.register(main.PoolUnit)
class PoolUnitAdmin(admin.ModelAdmin):
    pass


@admin.register(main.PoolCourse)
class PoolCourseAdmin(admin.ModelAdmin):
    pass
