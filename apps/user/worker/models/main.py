from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models


class WorkStatus(time_models.TimeStamp):
    for_staff = models.BooleanField(
        verbose_name=_("Personel İçin")
    )
    for_instructor = models.BooleanField(
        verbose_name=_("Eğitmen İçin")
    )
