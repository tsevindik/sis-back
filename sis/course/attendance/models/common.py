from ....common.models.schedule import Attendance


class AppAttendance(Attendance):
    pass

    class Meta:
        abstract = True
        app_label = 'attendance'
