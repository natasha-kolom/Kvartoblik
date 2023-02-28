from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from apartments.models import *


class BuildingProjectCreateSerializer(ModelSerializer):
    class Meta:
        model = BuildingProject
        fields = ('__all__')


class SectionSerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = ('name',)



class BuildingCreateSerializer(ModelSerializer):
    sections = SectionSerializer(many=True)

    class Meta:
        model = Building
        fields = ('name', 'project', 'sections')

    def create(self, validated_data):
        sections = validated_data.pop('sections')
        building = Building(**validated_data)
        building.save()
        serializer = SectionSerializer(data=sections, many=True)
        if serializer.is_valid(raise_exception=True):
            sections = serializer.save(building=building)
        return building





class BuildingProjectSerializer(ModelSerializer):
    building_count = serializers.IntegerField()
    section_count = serializers.IntegerField()
    apartment_count = serializers.IntegerField()

    class Meta:
        model = BuildingProject
        fields = ('name', 'address', 'building_count', 'section_count', 'apartment_count', 'image')



class ExplicationSerializer(ModelSerializer):
    class Meta:
        model = Explication
        fields = ('name', 'area')


class ApartmentSerializer(ModelSerializer):
    class Meta:
        model = Apartment
        fields = ('layout', 'floor')


class LayoutSerializer(ModelSerializer):
    class Meta:
        model = Layout
        fields = '__all__'


class LayoutCreateSerializer(ModelSerializer):
    explication = ExplicationSerializer(many=True)

    class Meta:
        model = Layout
        fields = ('name', 'number_of_rooms', 'total_area', 'living_area', 'image', 'explication')

    def create(self, validated_data):
        explication = validated_data.pop('explication')
        layout = Layout(**validated_data)
        layout.save()
        serializer = ExplicationSerializer(data=explication, many=True)
        if serializer.is_valid(raise_exception=True):
            explication = serializer.save(layout=layout)
        return layout


class FloorPlanSerializer(ModelSerializer):
    layout = ApartmentSerializer(source='apartment_set', many=True)
    class Meta:
        model = FloorPlan
        fields = ('floor', 'section', 'layout')


class BuildingSerializer(ModelSerializer):
    sections = SectionSerializer(many=True)
    class Meta:
        model = Building
        fields = ('id', 'name', 'project', 'sections')




class ApartmentsSaleSerializer(ModelSerializer):
    class Meta:
        model = ApartmentsSale
        fields = ('apartment', 'status', 'price')

class ApartmentDetailSerializer(ModelSerializer):
    layout = LayoutCreateSerializer()
    floor = SlugRelatedField(slug_field="floor", read_only=True)
    section = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    available_on_floors = serializers.SerializerMethodField()
    class Meta:
        model = Apartment
        fields = ('id', 'name', 'layout', 'floor', 'section', 'status', 'price', 'available_on_floors')

    def get_section(self, obj):
        query = FloorPlan.objects.filter(id=obj.floor_id)[0]
        serializer = FloorPlanSerializer(query)
        return serializer.data['section']

    def get_status(self, obj):
        query = ApartmentsSale.objects.filter(apartment=obj.id)[0]
        serializer = ApartmentsSaleSerializer(query)
        return serializer.data['status']

    def get_price(self, obj):
        query = ApartmentsSale.objects.filter(apartment=obj.id)[0]
        serializer = ApartmentsSaleSerializer(query)
        return serializer.data['price']

    def get_available_on_floors(self, obj):
        query = Apartment.objects.filter(layout=obj.layout)
        serializer = ApartmentSerializer(query, many=True)
        return serializer.data


class ApartmentSaleUpdatePriceSerializer(ModelSerializer):
    floor = serializers.SerializerMethodField(read_only=True)
    section = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = ApartmentsSale
        fields = ('apartment', 'price', 'floor', 'section', 'coef_floor', 'coef_rooms')

    def get_floor(self, obj):
        query = Apartment.objects.filter(id=obj.apartment_id)[0]
        serializer = ApartmentDetailSerializer(query)
        return serializer.data['floor']

    def get_section(self, obj):
        query = Apartment.objects.filter(id=obj.apartment_id)[0]
        serializer = ApartmentDetailSerializer(query)
        return serializer.data['section']

    def update(self, instance, validated_data):
        instance.apartment = validated_data.get('apartment', instance.apartment)
        price = instance.price*(instance.coef_floor+instance.coef_rooms)
        instance.price = price
        instance.coef_floor = validated_data.get('coef_floor', instance.coef_floor)
        instance.coef_rooms = validated_data.get('coef_rooms', instance.coef_rooms)
        instance.save()
        return instance


