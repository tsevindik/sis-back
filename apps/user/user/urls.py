from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    url(r'^authenticate/', obtain_jwt_token, name="authenticate"),
    url(r'^refresh-token/', refresh_jwt_token, name="refresh_token"),
    url(r'^verify-token/', verify_jwt_token, name="verify_token")
]