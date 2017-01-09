from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models, contact as contact_models
from config.settings.common import AUTH_USER_MODEL
from apps.user.user.models import WorkStatus


TIME_STATUS = (
    (0, _('Tam Zamanlı')),
    (1, _('Yarı Zamanlı'))
)


class UserProfile(time_models.TimeStamp):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("Kullanıcı")
    )
    id_no = models.CharField(
        max_length=20,
        verbose_name=_("Kimlik Numarası")
    )
    pass_no = models.CharField(
        max_length=20,
        verbose_name=_("Pasaport Numarası")
    )

    class Meta:
        abstract = True


class WorkerProfile(UserProfile):
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


class UserPhone(contact_models.Phone):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("Kullanıcı")
    )
    title = models.CharField(
        max_length=50,
        verbose_name=_("Başlık")
    )

    class Meta:
        abstract = True


class UserAddress(contact_models.Address):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("Kullanıcı")
    )
    title = models.CharField(
        max_length=50,
        verbose_name=_("Başlık")
    )
    description = models.TextField(
        verbose_name=_("Açıklama")
    )

    class Meta:
        abstract = True
