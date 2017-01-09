from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import main


@admin.register(main.Certification)
class CertificationAdmin(admin.ModelAdmin):
    pass
