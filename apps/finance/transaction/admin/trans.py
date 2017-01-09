from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import trans


@admin.register(trans.EmployeeTransactionTypeTrans)
class EmployeeTransactionTypeTransAdmin(admin.ModelAdmin):
    pass


@admin.register(trans.StudentTransactionTypeTrans)
class StudentTransactionTypeTransAdmin(admin.ModelAdmin):
    pass
