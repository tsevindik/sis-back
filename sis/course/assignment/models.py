from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...institute.institute.models import University
from ...common.models.schedule import CampusEvent, IMPLEMENTATION_TYPE
from ...common.models.time import TimeStamp, DateTimeInterval
from ..registry.models import SectionRegistry
from ..section.models import CourseSection


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
    university = models.ForeignKey(University)


class SectionAssignment(DateTimeInterval):
    type = models.ForeignKey(AssignmentType)
    section = models.ForeignKey(CourseSection)
    percentage = models.IntegerField(verbose_name=_("Yüzde"))
    implementation = models.CharField(
        max_length=1,
        choices=IMPLEMENTATION_TYPE,
        verbose_name=_("Uygulama Türü")
    )


class AssignmentGrade(TimeStamp):
    registry = models.ForeignKey(SectionRegistry)
    assignment = models.ForeignKey(SectionAssignment)
    grade = models.IntegerField(verbose_name=_("Not"))


class EventAssignmentSession(CampusEvent):
    assignment = models.ForeignKey(SectionAssignment)
