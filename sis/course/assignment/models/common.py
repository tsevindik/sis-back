from ....common.models.time import TimeStamp, DateTimeInterval
from ....common.models.schedule import CampusEvent


class AppTimeStamp(TimeStamp):
    pass

    class Meta:
        abstract = True
        app_label = 'assignment'


class AppDateTimeInterval(DateTimeInterval):
    pass

    class Meta:
        abstract = True
        app_label = 'assignment'


class AppCampusEvent(CampusEvent):
    pass

    class Meta:
        abstract = True
        app_label = 'assignment'
