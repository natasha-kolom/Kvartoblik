# Generated by Django 4.1.5 on 2023-02-16 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0008_alter_apartment_floor_remove_floorplan_layout_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='floorplan',
            name='layout',
        ),
        migrations.AddField(
            model_name='floorplan',
            name='layout',
            field=models.ManyToManyField(through='apartments.Apartment', to='apartments.layout'),
        ),
    ]
