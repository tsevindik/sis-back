from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import main


@admin.register(main.EmployeeAccount)
class EmployeeAccountAdmin(admin.ModelAdmin):
    pass


@admin.register(main.StudentAccount)
class StudentAccountAdmin(admin.ModelAdmin):
    pass
