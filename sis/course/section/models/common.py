from ....common.models.time import TimeStamp, DayTimeInterval
from ....common.models.schedule import CampusEvent


class AppTimeStamp(TimeStamp):
    pass

    class Meta:
        abstract = True
        app_label = 'section'


class AppDayTimeInterval(DayTimeInterval):
    pass

    class Meta:
        abstract = True
        app_label = 'section'


class AppCampusEvent(CampusEvent):
    pass

    class Meta:
        abstract = True
        app_label = 'section'
