from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.common import Type
from ...common.models.time import TimeStamp
from ...common.models.schedule import CampusPlaceEvent
from ..registry.models import SessionRegistry
from ..session.models import CourseSession


ASSIGNMENT_IMPLEMENTATION = (
    (0, _('Uzak')),
    (1, _('Yerel'))
)


class EventAssignmentType(Type):
    pass


class SessionEventAssignment(TimeStamp):
    type = models.ForeignKey(EventAssignmentType)
    session = models.ForeignKey(CourseSession)
    percentage = models.IntegerField(verbose_name=_("Yüzde"))
    implementation = models.CharField(
        max_length=1,
        choices=ASSIGNMENT_IMPLEMENTATION,
        verbose_name=_("Uygulama")
    )


class EventAssignmentSession(CampusPlaceEvent):
    assignment = models.ForeignKey(SessionEventAssignment)


class EventAssignmentGrade(TimeStamp):
    registry = models.ForeignKey(SessionRegistry)
    assignment = models.ForeignKey(EventAssignmentSession)
    grade = models.IntegerField(verbose_name=_("Not"))
