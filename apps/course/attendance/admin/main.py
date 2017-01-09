from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import main


@admin.register(main.StudentAttendanceStatus)
class StudentAttendanceStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(main.StudentCourseAttendance)
class StudentCourseAttendanceAdmin(admin.ModelAdmin):
    pass


@admin.register(main.EventAssignmentAttendance)
class EventAssignmentAttendanceAdmin(admin.ModelAdmin):
    pass


@admin.register(main.InstructorAttendanceStatus)
class InstructorAttendanceStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(main.InstructorCourseAttendance)
class InstructorCourseAttendanceAdmin(admin.ModelAdmin):
    pass
