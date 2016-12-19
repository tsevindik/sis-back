from django.utils.translation import ugettext_lazy as _
from django.db import models

from . import main
from config.settings.common import AUTH_USER_MODEL
from utils.models import time as time_models


class SectionAuth(time_models.TimeStamp):
    course_section = models.ForeignKey(
        main.CourseSection,
        verbose_name=_("Ders Grubu")
    )
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("Kullanıcı")
    )
