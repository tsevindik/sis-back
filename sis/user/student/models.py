from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...common.models.user import UserProfile, UserPhone, UserAddress


class StudentProfile(UserProfile):
    pass


class StudentPhone(UserPhone):
    pass


class StudentAddress(UserAddress):
    pass
