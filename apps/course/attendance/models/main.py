from django.utils.translation import ugettext_lazy as _
from django.db import models

from config.settings.common import AUTH_USER_MODEL
from apps.course.section.models import SectionSession
from apps.course.assignment.models import EventAssignmentSession
from utils.models import time as time_models


class AttendanceStatus(time_models.TimeStamp):
    status = models.BooleanField(
        verbose_name=_("Durum")
    )


class StudentAttendanceStatus(AttendanceStatus):
    pass


class StudentAttendance(time_models.TimeStamp):
    student_attendance_status = models.ForeignKey(
        StudentAttendanceStatus,
        verbose_name=_("Devam Durumu")
    )
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("Kullanıcı")
    )

    class Meta:
        abstract = True


class StudentSessionAttendance(StudentAttendance):
    session_session = models.ForeignKey(
        SectionSession,
        verbose_name=_("Oturum")
    )


class EventAssignmentAttendance(StudentAttendance):
    event_assignment_session = models.ForeignKey(
        EventAssignmentSession,
        verbose_name=_("Görev Oturumu")
    )


class InstructorAttendanceStatus(AttendanceStatus):
    pass


class InstructorSessionAttendance(time_models.TimeStamp):
    instructor_attendance_status = models.ForeignKey(
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
