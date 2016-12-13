from utils.models import time, contact
from ..apps import APP_NAME


class AppTimeStamp(time.TimeStamp):
    pass

    class Meta:
        abstract = True
        app_label = APP_NAME


class AppAddress(contact.Address):
    pass

    class Meta:
        abstract = True
        app_label = APP_NAME


class AppAddressTrans(contact.AddressTrans):
    pass

    class Meta:
        abstract = True
        app_label = APP_NAME
