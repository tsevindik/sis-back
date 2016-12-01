from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser

from ...institute.institute.models import University
from ...common.models.time import TimeStamp


class User(AbstractUser):
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Güncellenme Zamanı")
    )


class UserProfile(TimeStamp):
    user = models.ForeignKey(User)


class UserUniversity(TimeStamp):
    user = models.ForeignKey(User)
    university = models.ForeignKey(University)
    is_primary = models.BooleanField()
