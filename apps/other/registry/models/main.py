from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models
from apps.user.user.models import User
from apps.course.section.models import CourseSection


class SectionRegistry(time_models.TimeStamp):
    course_section = models.ForeignKey(
        CourseSection,
        verbose_name=_("Ders Grubu")
    )
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )
