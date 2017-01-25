from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models
from config.settings.common import AUTH_USER_MODEL
from apps.course.section.models import CourseSection


class SectionRegistry(time_models.TimeStamp):
    course_section = models.ForeignKey(
        CourseSection,
        verbose_name=_("Ders Grubu")
    )
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("Kullanıcı")
    )
