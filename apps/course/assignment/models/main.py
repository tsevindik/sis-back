from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models, schedule as schedule_models
from apps.course.section.models import CourseSection


ASSIGNMENT_FORMAT = (
    (0, _('Olay bazlı')),
    (1, _('Süreç bazlı'))
)


class AssignmentType(time_models.TimeStamp):
    format = models.CharField(
        max_length=1,
        choices=ASSIGNMENT_FORMAT,
        verbose_name=_("Format")
    )


class SectionAssignment(time_models.DateTimeInterval):
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
        choices=schedule_models.IMPLEMENTATION_TYPE,
        verbose_name=_("Uygulama Türü")
    )

    class Meta:
        abstract = True


class SectionProcessAssignment(SectionAssignment):
    pass


class SectionEventAssignment(time_models.TimeStamp):
    pass


class EventAssignmentSession(schedule_models.CampusEvent):
    section_event_assignment = models.ForeignKey(
        SectionEventAssignment,
        verbose_name=_("Grup Görevi")
    )
