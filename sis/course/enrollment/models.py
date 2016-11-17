from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.schedule import Attendance
from ...common.models.time import TimeStamp
from ...user.user.models import User
from ..session.models import CourseSession, CourseSessionLessonMeeting


class CourseSessionEnrollment(TimeStamp):
    course_session = models.ForeignKey(CourseSession)
    student = models.ForeignKey(User)


class LessonStudentAttendance(Attendance):
    course_session_lesson_meeting = models.ForeignKey(CourseSessionLessonMeeting)
    student = models.ForeignKey(User)


class EnrollmentGrade(TimeStamp):
    enrollment = models.ForeignKey(CourseSessionEnrollment)
    grade = models.IntegerField(verbose_name=_("Not"))
