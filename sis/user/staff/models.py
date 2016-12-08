from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.user import UserProfile, UserPhone, UserAddress, WORK_TIME


class StaffProfile(UserProfile):
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


class StaffPhone(UserPhone):
    pass


class StaffAddress(UserAddress):
    pass
