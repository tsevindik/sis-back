from ....common.models.time import TimeStamp
from ..apps import APP_NAME


class AppTimeStamp(TimeStamp):
    pass

    class Meta:
        abstract = True
        app_label = APP_NAME
