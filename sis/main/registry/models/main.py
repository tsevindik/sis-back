from django.utils.translation import ugettext_lazy as _
from django.db import models

from ....user.user.models import User
from ....course.section.models import CourseSection
from .common import AppTimeStamp


class SectionRegistry(AppTimeStamp):
    course_section = models.ForeignKey(
        CourseSection,
        verbose_name=_("Ders Grubu")
    )
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )
