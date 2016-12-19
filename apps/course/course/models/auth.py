from django.utils.translation import ugettext_lazy as _
from django.db import models

from . import main
from config.settings.common import AUTH_USER_MODEL
from utils.models import time as time_models


class CourseAuth(time_models.TimeStamp):
    course = models.ForeignKey(
        main.Course,
        verbose_name=_("Ders")
    )
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("Kullanıcı")
    )
