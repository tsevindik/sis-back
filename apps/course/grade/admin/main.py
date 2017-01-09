from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import main


@admin.register(main.LetterGrade)
class LetterGradeAdmin(admin.ModelAdmin):
    pass


@admin.register(main.SectionLetterGrade)
class SectionLetterGradeAdmin(admin.ModelAdmin):
    pass


@admin.register(main.RegistryGrade)
class RegistryGradeAdmin(admin.ModelAdmin):
    pass


@admin.register(main.AssignmentGrade)
class AssignmentGradeAdmin(admin.ModelAdmin):
    pass
