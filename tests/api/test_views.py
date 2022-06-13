from django.test import TestCase
from rest_framework.test import APIClient
from api.models import ServiceArea


class BaseSetTest:
    def setUp(self):
        self.client = APIClient()


class ServiceAreaSetTest(BaseSetTest, TestCase):
    fixtures = ["provider.json", "service_area.json"]

    def test_get_list_filter(self):
        """
        When a query parameter 'coordinates' is setted, a filtered list is returned
        """
        response = self.client.get("/api/service_area/?coordinates=21.1,21.1")
        self.assertEqual(response.json()["count"], 1)
        self.assertEqual(response.json()["next"], None)
        self.assertEqual(response.json()["results"][0]["id"], 19)

    def test_get_list_filter_error_parameter(self):
        """
        When 'coordinates' parameter is wrong, must ignore and return all list
        """
        response = self.client.get("/api/service_area/?coordinates=foo,bar")
        self.assertEqual(response.json()["count"], 48)

    def test_create_wrong_format_service_area(self):
        """
        When create a area with wrong format, must return 400 code
        """
        data = {
            "name": "test_wrong",
            "provider": 1,
            "price": 12.0,
            "area": "SRID=4326;POL ((4.0 5.0, 4.0 4.0, 5.0 4.0, 5.0 5.0, 4.0 5.0))",
        }
        response = self.client.post("/api/service_area/", data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json()["detail"],
            "String input unrecognized as WKT EWKT, and HEXEWKB.",
        )

    def test_update_wrong_format_service_area(self):
        """
        When update a area with wrong format, must return 400 code
        """
        data = {
            "name": "test_wrong",
            "provider": 1,
            "price": 12.0,
            "area": "SRID=4326;POL ((4.0 5.0, 4.0 4.0, 5.0 4.0, 5.0 5.0, 4.0 5.0))",
        }
        response = self.client.put("/api/service_area/2/", data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json()["detail"],
            "String input unrecognized as WKT EWKT, and HEXEWKB.",
        )
