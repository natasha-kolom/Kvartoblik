from django.db.models import Count
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from apartments.models import *
from apartments.serializers import *
from rest_framework.decorators import action


class BuildingProjectViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = BuildingProject.objects.all().annotate(
        building_count=Count('building', distinct=True),
        section_count=Count('building__sections', distinct=True),
        apartment_count=Count('building__sections__floorplan__apartment', distinct=True)
    )
    serializer_class = BuildingProjectSerializer

class BuildingProjectCreateViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = BuildingProject.objects.all()
    serializer_class = BuildingProjectCreateSerializer


class BuildingProjectUpdateDeleteViewSet(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = BuildingProject.objects.all()
    serializer_class = BuildingProjectCreateSerializer

class BuildingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class BuildingCreateViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Building.objects.all()
    serializer_class = BuildingCreateSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['project', 'name']



class SectionViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class LayoutViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Layout.objects.all()
    serializer_class = LayoutSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['number_of_rooms']


class LayoutCreateViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Layout.objects.all()
    serializer_class = LayoutCreateSerializer


class ExplicationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Explication.objects.all()
    serializer_class = ExplicationSerializer


class FloorPlanViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = FloorPlan.objects.all()
    serializer_class = FloorPlanSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        floorplan = FloorPlan.objects.create(floor=data['floor'], section_id=data['section'])
        floorplan.save()
        for layout in data['layout']:
            apartment_name = f"{data['section']}-{data['floor']}-{layout['layout']}"
            apartment = Apartment.objects.create(layout_id=layout['layout'], name=apartment_name, floor_id=floorplan.pk)
            apartment.save()
            apartment_sale = ApartmentsSale.objects.create(apartment_id=apartment.pk)
            apartment_sale.save()
            layout_obj = Layout.objects.get(id=layout['layout'])
            floorplan.layout.add(layout_obj)

        serializers = FloorPlanSerializer(floorplan)
        return Response(serializers.data)


class ApartmentDetailViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Apartment.objects.all()
    serializer_class = ApartmentDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['layout__number_of_rooms', 'floor__section']


class ApartmentsSaleViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ApartmentsSale.objects.all()
    serializer_class = ApartmentSaleUpdatePriceSerializer

