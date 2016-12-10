from ....common.models.time import TimeStamp
from ....common.models.contact import Address, AddressTrans
from ..apps import APP_NAME


class AppTimeStamp(TimeStamp):
    pass

    class Meta:
        abstract = True
        app_label = APP_NAME


class AppAddress(Address):
    pass

    class Meta:
        abstract = True
        app_label = APP_NAME


class AppAddressTrans(AddressTrans):
    pass

    class Meta:
        abstract = True
        app_label = APP_NAME
