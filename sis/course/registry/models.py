from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.time import TimeStamp
from ...user.user.models import User
from ..session.models import CourseSession, SessionLetterGrade


class SessionRegistry(TimeStamp):
    session = models.ForeignKey(CourseSession)
    student = models.ForeignKey(User)


class RegistryGrade(TimeStamp):
    registry = models.ForeignKey(SessionRegistry)
    numeric_grade = models.FloatField(verbose_name=_("Sayısal Not"))
    letter_grade = models.ForeignKey(SessionLetterGrade)
    rank = models.IntegerField(verbose_name=_("Sıra"))
    percentile = models.FloatField(verbose_name=_("Yüzdelik Dilim"))
