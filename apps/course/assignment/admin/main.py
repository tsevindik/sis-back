from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import main


@admin.register(main.AssignmentType)
class AssignmentTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(main.SectionProcessAssignment)
class SectionProcessAssignmentAdmin(admin.ModelAdmin):
    pass


@admin.register(main.SectionEventAssignment)
class SectionEventAssignmentAdmin(admin.ModelAdmin):
    pass


@admin.register(main.EventAssignmentSession)
class EventAssignmentSessionAdmin(admin.ModelAdmin):
    pass
