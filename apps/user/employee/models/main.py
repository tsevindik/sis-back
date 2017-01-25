from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...user.models import UserProfile
from utils.models import time as time_models


TIME_STATUS = (
    (0, _('Tam Zamanlı')),
    (1, _('Yarı Zamanlı'))
)


class WorkStatus(time_models.TimeStamp):
    for_staff = models.BooleanField(
        verbose_name=_("Personel İçin")
    )
    for_instructor = models.BooleanField(
        verbose_name=_("Eğitmen İçin")
    )


class EmployeeProfile(UserProfile):
    work_status = models.ForeignKey(
        WorkStatus,
        verbose_name=_("Çalışma Durumu")
    )
    time_status = models.CharField(
        max_length=1,
        choices=TIME_STATUS,
        verbose_name=_("Zaman Durumu")
    )
    work_hour = models.IntegerField(
        verbose_name=_("Çalışma Saati")
    )
    on_leave = models.BooleanField(
        verbose_name=_("İzinli")
    )
    is_quit = models.BooleanField(
        verbose_name=_("Ayrıldı")
    )

    class Meta:
        abstract = True
