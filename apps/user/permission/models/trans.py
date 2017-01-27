from django.utils.translation import ugettext_lazy as _
from django.db import models

from . import main


class MenuPermissionTrans(models.Model):
    neutral = models.ForeignKey(
        main.MenuPermission
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_("İsim")
    )
