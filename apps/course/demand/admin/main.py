from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import main


@admin.register(main.StudentQuotaDemand)
class StudentQuotaDemandAdmin(admin.ModelAdmin):
    pass


@admin.register(main.StudentCourseDemand)
class StudentCourseDemandAdmin(admin.ModelAdmin):
    pass


@admin.register(main.InstructorCourseDemand)
class InstructorCourseDemandAdmin(admin.ModelAdmin):
    pass
