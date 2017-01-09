from django.utils.translation import ugettext_lazy as _
from django.db import models

from apps.user.user.models import WorkStatus
from apps.user.utils import models as user_models


class StaffProfile(user_models.UserProfile):
    work_status = models.ForeignKey(
        WorkStatus,
        verbose_name=_("Çalışma Durumu")
    )
    work_time = models.CharField(
        max_length=1,
        choices=user_models.WORK_TIME,
        verbose_name=_("Çalışma Saati")
    )
    on_leave = models.BooleanField(
        verbose_name=_("İzinli")
    )
    is_quit = models.BooleanField(
        verbose_name=_("Ayrıldı")
    )


class StaffPhone(user_models.UserPhone):
    pass


class StaffAddress(user_models.UserAddress):
    pass
