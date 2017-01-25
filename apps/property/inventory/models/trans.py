from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import trans as trans_models
from . import main


class InventoryTypeTrans(trans_models.Translation):
    neutral = models.ForeignKey(
        main.Inventory
    )
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )


class InventoryTrans(trans_models.Translation):
    neutral = models.ForeignKey(
        main.Inventory
    )
    name = models.CharField(
        max_length=150,
        verbose_name=_("İsim")
    )
    description = models.TextField(
        verbose_name=_("Açıklama")
    )
