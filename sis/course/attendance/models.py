from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.schedule import Attendance
from ...user.user.models import User
from ..section.models import SectionSession
from ..assignment.models import EventAssignmentSession


class StudentCourseAttendance(Attendance):
    session_session = models.ForeignKey(
        SectionSession,
        verbose_name=_("Oturum")
    )
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )


class InstructorCourseAttendance(Attendance):
    session_session = models.ForeignKey(
        SectionSession,
        verbose_name=_("Oturum")
    )
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )


class EventAssignmentAttendance(Attendance):
    event_assignment_session = models.ForeignKey(
        EventAssignmentSession,
        verbose_name=_("Görev Oturumu")
    )
    user = models.ForeignKey(
        User,
        verbose_name=_("Kullanıcı")
    )
