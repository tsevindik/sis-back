from django.urls import reverse
from django.utils.translation import get_language

from rest_framework import status

from utils.rest.testcases import APIJWTTestCase
from .models import UniversityTrans, UniversityConfig


class UniversityConfigHomeTest(APIJWTTestCase):
    fixtures = ['test.json']
    url = reverse("api:institute:university_config_home")
    data = {"university_config":
                {"default_language": "tr", "major_count": 1, "major_gpa": 3.0, "minor_count": 1, "minor_gpa": 2.5},
            "university": {
                "trans": {"name": "Test Üniversitesi", "language_code": "tr", "neutral": 1},
                "neutral": {"official_name": "University of Test"}}}

    def test_can_read(self):
        response = self.client.get(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        try:
            UniversityTrans.objects.get_by_language(get_language())
            self.assertEquals(response.data, self.data)
        except UniversityTrans.DoesNotExist:
            university_config = UniversityConfig.objects.get_single()
            self.data["university"]["trans"]["language_code"] = university_config.default_language
            self.assertEqual(response.data, self.data)


class PrimaryUniversityTest(APIJWTTestCase):
    fixtures = ['test.json']
    url = reverse("api:institute:primary_university")
    data = {"official_name": "University of Test"}

    def test_can_put(self):
        response = self.client.put(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.data)


class UniversityTransTest(APIJWTTestCase):
    fixtures = ['test.json']
    create_data = {"neutral": 1, "name": "University of Test", "language_code": "en"}
    read_data = {"neutral": 1, "name": "Test Üniversitesi", "language_code": "tr"}

    def test_can_create(self):
        url = reverse("api:institute:university_trans")
        response = self.client.post(url, self.create_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, self.create_data)

    def test_can_read_by_neutral_id(self):
        url = reverse("api:institute:university_trans_by_id", kwargs={'neutral': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [self.read_data])

    def test_can_read_by_neutral_id_language(self):
        url = reverse("api:institute:university_trans_by_id_language", kwargs={"neutral": 1, "language_code": "tr"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.read_data)

    def test_can_update_by_neutral_id_language(self):
        url = reverse("api:institute:university_trans_by_id_language", kwargs={"neutral": 1, "language_code": "tr"})
        response = self.client.put(url, self.create_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.create_data)

    def test_can_delete_by_neutral_id_language(self):
        url = reverse("api:institute:university_trans_by_id_language", kwargs={"neutral": 1, "language_code": "tr"})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class UniversityConfigTest(APIJWTTestCase):
    fixtures = ['test.json']
    url = reverse("api:institute:university_config")
    data = {"default_language": "tr", "major_count": 1, "major_gpa": 3.0, "minor_count": 1, "minor_gpa": 2.5}

    def test_can_put(self):
        response = self.client.put(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.data)
