from django.db import models
from django_filters.rest_framework import DjangoFilterBackend


class BuildingProject(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="photo_buildingProject/%Y/%m/%d")

    def __str__(self):
        return f'{self.name}'



class Building(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(BuildingProject, on_delete=models.PROTECT, related_name='building')


    def __str__(self):
        return f'{self.name}'



class Section(models.Model):
    name = models.CharField(max_length=255)
    building = models.ForeignKey(Building, on_delete=models.PROTECT, related_name='sections')

    def __str__(self):
        return f'{self.id} {self.name}'


class Layout(models.Model):
    name = models.CharField(max_length=255)
    number_of_rooms = models.IntegerField()
    total_area = models.DecimalField(max_digits=7, decimal_places=2)
    living_area = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to="photo_layout/%Y/%m/%d", null=True)

    def __str__(self):
        return f'{self.name}'


class Explication(models.Model):
    name = models.CharField(max_length=255)
    area = models.DecimalField(max_digits=7, decimal_places=2)
    layout = models.ForeignKey(Layout, on_delete=models.PROTECT, related_name='explication')

    def __str__(self):
        return f'Планування {self.layout}, {self.name} {self.area} м.кв'


class FloorPlan(models.Model):
    floor = models.IntegerField()
    section = models.ForeignKey('Section', on_delete=models.PROTECT, related_name='floorplan')
    image = models.ImageField(upload_to="photo_floorplan/%Y/%m/%d")
    layout = models.ManyToManyField(Layout, through='Apartment')

    def __str__(self):
        return f'{self.floor} поверх'


class Apartment(models.Model):
    name = models.CharField(max_length=255)
    layout = models.ForeignKey(Layout, on_delete=models.PROTECT)
    floor = models.ForeignKey(FloorPlan, on_delete=models.PROTECT)


    def __str__(self):
        return f'{self.name}'


class ApartmentsSale(models.Model):
    STATUS = (
        (1, 'For Sale'),
        (2, 'Booked'),
        (3, 'Sold')
    )

    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='apartment')
    status = models.PositiveSmallIntegerField(choices=STATUS, default=1)
    time_update = models.DateTimeField(auto_now=True)
    coef_floor = models.DecimalField(max_digits=5, decimal_places=3, default=0.5)
    coef_rooms = models.DecimalField(max_digits=5, decimal_places=3, default=0.5)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=1)

    def __str__(self):
        return f'Квартира {self.apartment} {self.status} Обновлена {self.time_update}'




