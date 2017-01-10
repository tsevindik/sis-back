from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser

from utils.models import time as time_models
from apps.institute.institute.models import University


class User(AbstractUser):
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Güncellenme Zamanı")
    )
    registered_multiple_degree = models.BooleanField(
        verbose_name=_("Çoklu Programa Kayıtlı")
    )


class UserUniversity(time_models.TimeStamp):
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )


class WorkStatus(time_models.TimeStamp):
    for_staff = models.BooleanField(
        verbose_name=_("Personel İçin")
    )
    for_instructor = models.BooleanField(
        verbose_name=_("Eğitmen İçin")
    )
