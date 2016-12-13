from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.institute.institute.models import University
from .utils import AppTimeStamp


class User(AbstractUser):
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Güncellenme Zamanı")
    )


class UserUniversity(AppTimeStamp):
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )
    is_primary = models.BooleanField(
        verbose_name=_("Birincil")
    )
