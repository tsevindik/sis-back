from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.common import Type
from ...common.models.schedule import Event
from ...institution.schedule.models import AcademicSemester
from ..session.models import CourseSession


ASSIGNMENT_IMPLEMENTATION = (
    (0, _('Uzak')),
    (1, _('Yerel'))
)


class AssignmentType(Type):
    pass


class Assignment(Event):
    type = models.ForeignKey(AssignmentType)
    course_session = models.ForeignKey(CourseSession)
    semester = models.ForeignKey(AcademicSemester)
    percentage = models.IntegerField(verbose_name=_("Yüzde"))
    implementation = models.CharField(
        max_length=1,
        choices=ASSIGNMENT_IMPLEMENTATION,
        verbose_name=_("Uygulama")
    )