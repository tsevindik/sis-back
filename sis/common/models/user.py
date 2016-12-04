from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...user.user.models import User
from ..models.time import TimeStamp


class UserProfile(TimeStamp):
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )

    class Meta:
        abstract = True
