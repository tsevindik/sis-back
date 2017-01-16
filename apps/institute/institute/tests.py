import json

from django.urls import reverse
from django.utils.translation import get_language
from rest_framework.test import APITestCase
from rest_framework import status

from .models import UniversityTrans, UniversityConfig


class UniversityConfigTests(APITestCase):
    fixtures = ['test.json']
    url = reverse("api:institute:university_config")

    def test_can_read(self):
        response = self.client.get(self.url)
        content = response.content.decode("utf8")
        data = json.loads(content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(data["university_config"]["major_gpa"], 3.0)
        self.assertEquals(data["university_config"]["minor_count"], 1)
        self.assertEquals(data["university"]["neutral"]["is_primary"], True)
        try:
            UniversityTrans.objects.get_by_language(get_language())
            self.assertEquals(data["university"]["trans"]["language_code"], get_language())
        except UniversityTrans.DoesNotExist:
            university_config = UniversityConfig.objects.get()
            self.assertEquals(data["university"]["trans"]["language_code"], university_config.default_language)
