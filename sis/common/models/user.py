from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.contact import Phone, Address, AddressTrans
from ...user.user.models import User
from ..models.time import TimeStamp


class UserProfile(TimeStamp):
    user = models.ForeignKey(
        User,
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


class UserPhone(Phone):
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )
    title = models.CharField(
        max_length=50,
        verbose_name=_("Başlık")
    )

    class Meta:
        abstract = True


class UserAddress(Address, AddressTrans):
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )
    title = models.CharField(
        max_length=50,
        verbose_name=_("Başlık")
    )

    class Meta:
        abstract = True
