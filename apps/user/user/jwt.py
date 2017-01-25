from calendar import timegm
from datetime import datetime

from rest_framework_jwt.settings import api_settings


def jwt_payload_handler(user=None):
    return {
        'username': user.username,
        'user_id': user.pk,
        'user_type': user_type(user),
        'orig_iat': timegm(datetime.utcnow().utctimetuple()),
        'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA,
    }


def user_type(user):
    if user.is_student:
        return 0
    elif user.is_instructor:
        return 1
    elif user.is_superuser:
        return 2
    else:
        return 3
