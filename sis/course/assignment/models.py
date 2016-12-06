from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...institute.institute.models import University
from ...common.models.schedule import CampusEvent, IMPLEMENTATION_TYPE
from ...common.models.time import TimeStamp, DateTimeInterval
from ..section.models import CourseSection


ASSIGNMENT_FORMAT = (
    (0, _('Olay bazlı')),
    (1, _('Süreç bazlı'))
)


class AssignmentType(TimeStamp):
    name = models.CharField(
        max_length=50,
        verbose_name=_("İsim")
    )
    format = models.CharField(
        max_length=1,
        choices=ASSIGNMENT_FORMAT,
        verbose_name=_("Format")
    )
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )


class SectionProcessAssignment(DateTimeInterval):
    assignment_type = models.ForeignKey(
        AssignmentType,
        verbose_name=_("Görev Türü")
    )
    course_section = models.ForeignKey(
        CourseSection,
        verbose_name=_("Ders Grubu")
    )
    percentage = models.IntegerField(
        verbose_name=_("Yüzde")
    )
    out_of_grade = models.IntegerField(
        verbose_name=_("Not Üzerinden")
    )
    implementation_type = models.CharField(
        max_length=1,
        choices=IMPLEMENTATION_TYPE,
        verbose_name=_("Uygulama Türü")
    )


class SectionEventAssignment(TimeStamp):
    assignment_type = models.ForeignKey(
        AssignmentType,
        verbose_name=_("Görev Türü")
    )
    course_section = models.ForeignKey(
        CourseSection,
        verbose_name=_("Ders Grubu")
    )
    percentage = models.IntegerField(
        verbose_name=_("Yüzde")
    )
    out_of_grade = models.IntegerField(
        verbose_name=_("Not Üzerinden")
    )
    implementation_type = models.CharField(
        max_length=1,
        choices=IMPLEMENTATION_TYPE,
        verbose_name=_("Uygulama Türü")
    )


class EventAssignmentSession(CampusEvent):
    section_event_assignment = models.ForeignKey(
        SectionEventAssignment,
        verbose_name=_("Grup Görevi")
    )
