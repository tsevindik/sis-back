from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.user import UserProfile, UserPhone, UserAddress


class StaffProfile(UserProfile):
    pass


class StaffPhone(UserPhone):
    pass


class StaffAddress(UserAddress):
    pass
