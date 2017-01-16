from django.conf.urls import url

from .views import UniversityConfigApi

urlpatterns = [
    url(r'^university-config/$', UniversityConfigApi.as_view(), name="university_config"),
]
