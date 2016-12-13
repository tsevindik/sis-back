from utils.models import time, schedule
from ..apps import APP_NAME


class AppTimeStamp(time.TimeStamp):
    pass

    class Meta:
        abstract = True
        app_label = APP_NAME


class AppDayTimeInterval(time.DayTimeInterval):
    pass

    class Meta:
        abstract = True
        app_label = APP_NAME


class AppCampusEvent(schedule.CampusEvent):
    pass

    class Meta:
        abstract = True
        app_label = APP_NAME
