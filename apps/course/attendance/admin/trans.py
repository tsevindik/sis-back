from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import trans


@admin.register(trans.StudentAttendanceStatusTrans)
class StudentAttendanceStatusTransAdmin(admin.ModelAdmin):
    pass


@admin.register(trans.InstructorAttendanceStatusTrans)
class InstructorAttendanceStatusTransAdmin(admin.ModelAdmin):
    pass
