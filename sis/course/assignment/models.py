from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.time import TimeStamp, DateTimeInterval
from ...common.models.schedule import CampusEvent
from ..registry.models import SessionRegistry
from ..session.models import CourseSession


ASSIGNMENT_IMPLEMENTATION = (
    (0, _('Uzak')),
    (1, _('Yerel'))
)

ASSIGNMENT_TYPE = (
    (0, _('Olay bazlı')),
    (1, _('Süreç bazlı'))
)


class AssignmentType(TimeStamp):
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )
    type = models.CharField(
        max_length=1,
        choices=ASSIGNMENT_TYPE,
        verbose_name=_("Tür")
    )


class SessionAssignment(DateTimeInterval):
    type = models.ForeignKey(AssignmentType)
    session = models.ForeignKey(CourseSession)
    percentage = models.IntegerField(verbose_name=_("Yüzde"))
    implementation = models.CharField(
        max_length=1,
        choices=ASSIGNMENT_IMPLEMENTATION,
        verbose_name=_("Uygulama")
    )


class EventAssignmentSession(CampusEvent):
    assignment = models.ForeignKey(SessionAssignment)


class AssignmentGrade(TimeStamp):
    registry = models.ForeignKey(SessionRegistry)
    assignment = models.ForeignKey(SessionAssignment)
    grade = models.IntegerField(verbose_name=_("Not"))
