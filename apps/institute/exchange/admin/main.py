from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from ..models import main


@admin.register(main.ExchangeProgram)
class ExchangeProgramAdmin(admin.ModelAdmin):
    pass


@admin.register(main.ExchangeAgreement)
class ExchangeAgreementAdmin(admin.ModelAdmin):
    pass


@admin.register(main.ExchangeApplication)
class ExchangeApplicationAdmin(admin.ModelAdmin):
    pass


@admin.register(main.ExchangeStudent)
class ExchangeStudentAdmin(admin.ModelAdmin):
    pass
