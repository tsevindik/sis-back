from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import main


@admin.register(main.EmployeeTransactionType)
class EmployeeTransactionTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(main.EmployeeTransaction)
class EmployeeTransactionAdmin(admin.ModelAdmin):
    pass


@admin.register(main.StudentTransactionType)
class StudentTransactionTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(main.StudentTransaction)
class StudentTransactionAdmin(admin.ModelAdmin):
    pass
