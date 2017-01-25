from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...user.models import UserAddress, UserPhone
from ...employee.models import EmployeeProfile


class StaffProfile(EmployeeProfile):
    pass


class StaffPhone(UserPhone):
    pass


class StaffAddress(UserAddress):
    pass
