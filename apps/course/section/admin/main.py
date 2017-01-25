from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import main


@admin.register(main.CourseSection)
class CourseSectionAdmin(admin.ModelAdmin):
    pass


@admin.register(main.SectionInstructor)
class SectionInstructorAdmin(admin.ModelAdmin):
    pass


@admin.register(main.SectionWeekSession)
class SectionWeekSessionAdmin(admin.ModelAdmin):
    pass


@admin.register(main.SectionSession)
class SectionSessionAdmin(admin.ModelAdmin):
    pass
