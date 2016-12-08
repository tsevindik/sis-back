from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models import WORK_TIME
from .common import AppUserProfile, AppUserAddress, AppUserPhone


class StaffProfile(AppUserProfile):
    work_time = models.CharField(
        max_length=1,
        choices=WORK_TIME,
        verbose_name=_("Çalışma Saati")
    )
    on_leave = models.BooleanField(
        verbose_name=_("İzinli")
    )
    is_quit = models.BooleanField(
        verbose_name=_("Ayrıldı")
    )


class StaffPhone(AppUserPhone):
    pass


class StaffAddress(AppUserAddress):
    pass
