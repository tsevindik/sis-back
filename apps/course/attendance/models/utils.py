from utils.models import schedule
from ..apps import APP_NAME


class AppAttendance(schedule.Attendance):
    pass

    class Meta:
        abstract = True
        app_label = APP_NAME
