from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import main


@admin.register(main.ProgramTuitionFee)
class ProgramTuitionFeeAdmin(admin.ModelAdmin):
    pass


@admin.register(main.ProgramCreditFee)
class ProgramCreditFeeAdmin(admin.ModelAdmin):
    pass
