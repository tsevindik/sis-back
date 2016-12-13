from utils.models import time
from ..apps import APP_NAME


class AppTimeStamp(time.TimeStamp):
    pass

    class Meta:
        abstract = True
        app_label = APP_NAME


class AppDateInterval(time.DateInterval):
    pass

    class Meta:
        abstract = True
        app_label = APP_NAME
