# Generated by Django 4.1.5 on 2023-02-17 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0009_remove_floorplan_layout_floorplan_layout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='price',
        ),
        migrations.AddField(
            model_name='apartmentssale',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=15),
        ),
    ]