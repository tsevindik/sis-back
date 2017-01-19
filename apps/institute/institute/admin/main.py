from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import main


@admin.register(main.University)
class UniversityAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        try:
            if request.data["is_primary"]:
                main.University.objects.get_primary()
            return False
        except main.University.DoesNotExist:
            return True


@admin.register(main.UniversityConfig)
class UniversityConfigAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = main.UniversityConfig.objects.all().count()
        if count == 0:
            return True
        return False


@admin.register(main.UniversityCourse)
class UniversityCourseAdmin(admin.ModelAdmin):
    pass
