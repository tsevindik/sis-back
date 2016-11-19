from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.common import Type
from ...common.models.time import TimeStamp
from ...common.models.schedule import Event
from ...institute.schedule.models import YearSemester
from ..registry.models import SessionRegistry
from ..session.models import CourseSession


ASSIGNMENT_IMPLEMENTATION = (
    (0, _('Uzak')),
    (1, _('Yerel'))
)


class AssignmentType(Type):
    pass


class SessionAssignment(Event):
    type = models.ForeignKey(AssignmentType)
    session = models.ForeignKey(CourseSession)
    semester = models.ForeignKey(YearSemester)
    percentage = models.IntegerField(verbose_name=_("Yüzde"))
    implementation = models.CharField(
        max_length=1,
        choices=ASSIGNMENT_IMPLEMENTATION,
        verbose_name=_("Uygulama")
    )


class AssignmentGrade(TimeStamp):
    registry = models.ForeignKey(SessionRegistry)
    assignment = models.ForeignKey(SessionAssignment)
    grade = models.IntegerField(verbose_name=_("Not"))