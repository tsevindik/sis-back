from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import trans


@admin.register(trans.YearTrans)
class YearTransAdmin(admin.ModelAdmin):
    pass


@admin.register(trans.YearSemesterTrans)
class YearSemesterTransAdmin(admin.ModelAdmin):
    pass


@admin.register(trans.SemesterCalendarTrans)
class SemesterCalendarTransAdmin(admin.ModelAdmin):
    pass


@admin.register(trans.CalendarPeriodTrans)
class CalendarPeriodTransAdmin(admin.ModelAdmin):
    pass
