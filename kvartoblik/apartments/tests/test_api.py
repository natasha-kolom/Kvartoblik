from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apartments.models import BuildingProject
from apartments.serializers import BuildingProjectCreateSerializer


class BuildingProjectApiTestCase(APITestCase):
    def test_get(self):
        building_project_1 = BuildingProject.objects.create(
            name='Test Project 1',
            address='Address 1',
            description='Description Project 1')

        building_project_2 = BuildingProject.objects.create(
            name='Test Project 2',
            address='Address 2',
            description='Description Project 2')
        url = reverse('projectcreate-list')
        response = self.client.get(url)
        serializer_data = BuildingProjectCreateSerializer([building_project_1, building_project_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)




