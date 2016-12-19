from django.utils.translation import ugettext_lazy as _
from django.db import models

from .main import Course
from apps.user.user.models import User
from utils.models import time as time_models


class CourseAuth(time_models.TimeStamp):
    course = models.ForeignKey(
        Course,
        verbose_name=_("Ders")
    )
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )
