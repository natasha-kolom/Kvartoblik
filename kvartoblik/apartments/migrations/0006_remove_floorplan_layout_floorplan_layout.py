# Generated by Django 4.1.5 on 2023-02-12 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0005_floorplan_layout'),
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
