import json

from django.urls import reverse
from django.utils.translation import get_language
from rest_framework.test import APITestCase
from rest_framework import status

from .models import UniversityTrans, UniversityConfig


class UniversityConfigHomeTest(APITestCase):
    fixtures = ['test.json']
    url = reverse("api:institute:university_config_home")

    # TODO: Find a better way
    def test_can_read(self):
        response = self.client.get(self.url)
        content = response.content.decode("utf8")
        data = json.loads(content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(data["university_config"]["major_gpa"], 3.0)
        self.assertEquals(data["university_config"]["minor_count"], 1)

        try:
            UniversityTrans.objects.get_by_language(get_language())
            self.assertEquals(data["university"]["trans"]["language_code"], get_language())
        except UniversityTrans.DoesNotExist:
            university_config = UniversityConfig.objects.get()
            self.assertEquals(data["university"]["trans"]["language_code"], university_config.default_language)


class PrimaryUniversityTest(APITestCase):
    fixtures = ['test.json']
    url = reverse("api:institute:primary_university")
    data = {"official_name": "University of Test"}

    def test_can_put(self):
        response = self.client.put(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.data)


class UniversityTransTest(APITestCase):
    fixtures = ['test.json']
    data = {"neutral": 1, "name": "Test Üniversitesi", "language_code": "tr"}

    def test_can_create(self):
        url = reverse("api:institute:university_trans")
        response = self.client.post(url, self.data)
        response_data = response.content.decode("utf8")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertJSONEqual(response_data, self.data)

    def test_can_read_by_neutral_id(self):
        url = reverse("api:institute:university_trans_by_id", kwargs={'neutral': 1})
        response = self.client.get(url)
        response_data = response.content.decode("utf8")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(response_data, [self.data])

    def test_can_read_by_neutral_id_language(self):
        url = reverse("api:institute:university_trans_by_id_language", kwargs={"neutral": 1, "language_code": "tr"})
        response = self.client.get(url)
        response_data = response.content.decode("utf8")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(response_data, self.data)


class UniversityConfigTest(APITestCase):
    fixtures = ['test.json']
    url = reverse("api:institute:university_config")
    data = {"default_language": "tr", "major_count": 1, "major_gpa": 3.0, "minor_count": 1, "minor_gpa": 2.5}

    def test_can_put(self):
        response = self.client.put(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.data)
