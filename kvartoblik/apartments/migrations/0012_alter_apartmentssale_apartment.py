# Generated by Django 4.1.5 on 2023-02-19 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0011_apartmentssale_coef_floor_apartmentssale_coef_rooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentssale',
            name='apartment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apartment', to='apartments.apartment'),
        ),
    ]