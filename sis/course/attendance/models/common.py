from ....common.models.schedule import Attendance
from ..apps import APP_NAME


class AppAttendance(Attendance):
    pass

    class Meta:
        abstract = True
        app_label = APP_NAME
