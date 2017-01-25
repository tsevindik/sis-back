from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models
from config.settings.common import AUTH_USER_MODEL
from apps.institute.institute.models import University


class ExchangeProgram(time_models.TimeStamp):
    pass


class ExchangeAgreement(time_models.TimeStamp):
    exchange_program = models.ForeignKey(
        ExchangeProgram,
        blank=True,
        null=True,
        verbose_name=_("Değişim Programı")
    )
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )


class ExchangeApplication(time_models.TimeStamp):
    exchange_agreement = models.ForeignKey(
        ExchangeAgreement,
        verbose_name=_("Değişim Anlaşması")
    )
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("Kullanıcı")
    )
    is_approved = models.BooleanField(
        verbose_name=_("Onaylandı")
    )


class ExchangeStudent(time_models.TimeStamp):
    exchange_agreement = models.ForeignKey(
        ExchangeAgreement,
        verbose_name=_("Değişim Anlaşması")
    )
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("Kullanıcı")
    )
