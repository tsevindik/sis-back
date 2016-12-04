from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.time import TimeStamp
from ...user.user.models import User
from ..section.models import CourseSection


class SectionRegistry(TimeStamp):
    course_section = models.ForeignKey(
        CourseSection,
        verbose_name=_("Ders Grubu")
    )
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )
