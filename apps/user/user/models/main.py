from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.institute.institute.models import University
from utils.models import time as time_models, contact as contact_models
from config.settings.common import AUTH_USER_MODEL


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

    class Meta:
        abstract = True


class User(AbstractUser):
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Güncellenme Zamanı")
    )
    is_student = models.BooleanField(
        default=False,
        verbose_name=_("Öğrenci")
    )
    is_instructor = models.BooleanField(
        default=False,
        verbose_name=_("Eğitmen")
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_("Personel")
    )
    registered_multiple_degree = models.BooleanField(
        default=False,
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

