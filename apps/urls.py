"""sis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from .user.user import urls as user_urls
from .institute.institute import urls as institute_urls

api_urls = [
    url(r'^auth/', include(user_urls, namespace="auth")),
    url(r'^institute/', include(institute_urls, namespace="institute")),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls, name="admin"),
    url(r'^', include(api_urls, namespace="api")),
]
