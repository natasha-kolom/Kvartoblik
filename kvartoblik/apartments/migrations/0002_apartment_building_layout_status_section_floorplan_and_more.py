# Generated by Django 4.1.5 on 2023-01-29 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='apartments.buildingproject')),
            ],
        ),
        migrations.CreateModel(
            name='Layout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number_of_rooms', models.IntegerField()),
                ('total_area', models.DecimalField(decimal_places=2, max_digits=7)),
                ('living_area', models.DecimalField(decimal_places=2, max_digits=7)),
                ('image', models.ImageField(upload_to='photo_layout/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='apartments.building')),
            ],
        ),
        migrations.CreateModel(
            name='FloorPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor', models.IntegerField()),
                ('image', models.ImageField(upload_to='photo_floorplan/%Y/%m/%d')),
                ('layout', models.ManyToManyField(through='apartments.Apartment', to='apartments.layout')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='apartments.section')),
            ],
        ),
        migrations.CreateModel(
            name='Explication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('area', models.DecimalField(decimal_places=2, max_digits=7)),
                ('layout', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='apartments.layout')),
            ],
        ),
        migrations.CreateModel(
            name='ApartmentsSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartments.apartment')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='apartments.status')),
            ],
        ),
        migrations.AddField(
            model_name='apartment',
            name='floor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='apartments.floorplan'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='layout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='apartments.layout'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='apartments.section'),
        ),
    ]
