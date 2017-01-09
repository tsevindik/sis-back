from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import main


@admin.register(main.Year)
class YearAdmin(admin.ModelAdmin):
    pass


@admin.register(main.YearSemester)
class YearSemesterAdmin(admin.ModelAdmin):
    pass


@admin.register(main.SemesterCalendar)
class SemesterCalendarAdmin(admin.ModelAdmin):
    pass


@admin.register(main.CalendarPeriod)
class CalendarPeriodAdmin(admin.ModelAdmin):
    pass
