from django.urls import reverse

from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework_jwt.settings import api_settings


class APIJWTAuthenticatedClient(APIClient):
    def login(self, username, password):
        url = reverse("api:auth:authenticate")
        response = self.post(url, {"username": username, "password": password})
        if response.status_code == status.HTTP_200_OK:
            self.credentials(
                HTTP_AUTHORIZATION="{0} {1}".format(api_settings.JWT_AUTH_HEADER_PREFIX, response.data['token']))

            return True
        else:
            return False

    def __init__(self, *args, **kwargs):
        super(APIJWTAuthenticatedClient, self).__init__(*args, **kwargs)
        self.login("testuser", "testpass")


class APIJWTTestCase(APITestCase):
    client_class = APIJWTAuthenticatedClient
