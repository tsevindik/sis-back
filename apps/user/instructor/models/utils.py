from utils.models import time
from apps.user.utils.models import UserProfile, UserAddress, UserPhone
from ..apps import APP_NAME


class AppTimeStamp(time.TimeStamp):
    pass

    class Meta:
        abstract = True
        app_label = APP_NAME


class AppUserProfile(UserProfile):
    pass

    class Meta:
        abstract = True
        app_label = APP_NAME


class AppUserAddress(UserAddress):
    pass

    class Meta:
        abstract = True
        app_label = APP_NAME


class AppUserPhone(UserPhone):
    pass

    class Meta:
        abstract = True
        app_label = APP_NAME
