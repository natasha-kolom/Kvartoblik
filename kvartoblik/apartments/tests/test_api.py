from django.urls import reverse
from rest_framework.test import APITestCase

class BuildingProjectApiTestCase(APITestCase):
    def test_get(self):

        url = reverse('project-list')
        #url = reverse('projects-detail')
        print(url)
        response = self.client.get(url)
        print(response)
