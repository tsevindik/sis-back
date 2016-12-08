from ....common.models.time import TimeStamp


class AppTimeStamp(TimeStamp):
    pass

    class Meta:
        abstract = True
        app_label = 'grade'
