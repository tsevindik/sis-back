from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...other.contact.models import Language
from ...common.models.time import TimeStamp
from . import models as inventory_models


class AssetTypeTrans(TimeStamp):
    neutral = models.ForeignKey(
        inventory_models.AssetType
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_("İsim")
    )


class AssetTrans(TimeStamp):
    neutral = models.ForeignKey(
        inventory_models.Asset
    )
    language = models.ForeignKey(
        Language,
        verbose_name=_("Dil")
    )
    name = models.CharField(
        max_length=200,
        verbose_name=_("İsim")
    )

