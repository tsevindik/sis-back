from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.user import UserProfile, UserAddress, UserPhone


class InstructorProfile(UserProfile):
    pass


class InstructorPhone(UserPhone):
    pass


class InstructorAddress(UserAddress):
    pass
