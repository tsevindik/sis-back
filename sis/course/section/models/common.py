from ....common.models.time import TimeStamp, DayTimeInterval
from ....common.models.schedule import CampusEvent
from ..apps import APP_NAME


class AppTimeStamp(TimeStamp):
    pass

    class Meta:
        abstract = True
        app_label = APP_NAME


class AppDayTimeInterval(DayTimeInterval):
    pass

    class Meta:
        abstract = True
        app_label = APP_NAME


class AppCampusEvent(CampusEvent):
    pass

    class Meta:
        abstract = True
        app_label = APP_NAME
