from django.utils.translation import ugettext_lazy as _
from django.db import models

from ....user.user.models import User
from ...institute.models import University
from .common import AppTimeStamp


class ExchangeProgram(AppTimeStamp):
    pass


class ExchangeAgreement(AppTimeStamp):
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
    out_university = models.ForeignKey(
        University,
        verbose_name=_("Gidilen Üniversite")
    )


class ExchangeApplication(AppTimeStamp):
    exchange_agreement = models.ForeignKey(
        ExchangeAgreement,
        verbose_name=_("Değişim Anlaşması")
    )
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )
    is_approved = models.BooleanField(
        verbose_name=_("Onaylandı")
    )


class ExchangeStudent(AppTimeStamp):
    exchange_agreement = models.ForeignKey(
        ExchangeAgreement,
        verbose_name=_("Değişim Anlaşması")
    )
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )
