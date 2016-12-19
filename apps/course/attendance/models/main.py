from django.utils.translation import ugettext_lazy as _
from django.db import models

from config.settings.common import AUTH_USER_MODEL
from apps.course.section.models import SectionSession
from apps.course.assignment.models import EventAssignmentSession
from utils.models import status as status_models, time as time_models


class StudentAttendanceStatus(status_models.BoolStatus):
    pass


class StudentCourseAttendance(time_models.TimeStamp):
    student_attendance_status = models.ForeignKey(
        StudentAttendanceStatus,
        verbose_name=_("Devam Durumu")
    )
    session_session = models.ForeignKey(
        SectionSession,
        verbose_name=_("Oturum")
    )
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("Kullanıcı")
    )


class EventAssignmentAttendance(time_models.TimeStamp):
    student_attendance_status = models.ForeignKey(
        StudentAttendanceStatus,
        verbose_name=_("Devam Durumu")
    )
    event_assignment_session = models.ForeignKey(
        EventAssignmentSession,
        verbose_name=_("Görev Oturumu")
    )
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("Kullanıcı")
    )


class InstructorAttendanceStatus(status_models.BoolStatus):
    pass


class InstructorCourseAttendance(time_models.TimeStamp):
    student_attendance_status = models.ForeignKey(
        InstructorAttendanceStatus,
        verbose_name=_("Devam Durumu")
    )
    session_session = models.ForeignKey(
        SectionSession,
        verbose_name=_("Oturum")
    )
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("Kullanıcı")
    )
