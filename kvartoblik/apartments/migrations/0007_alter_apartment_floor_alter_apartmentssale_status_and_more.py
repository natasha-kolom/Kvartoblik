# Generated by Django 4.1.5 on 2023-02-13 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0006_remove_floorplan_layout_floorplan_layout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='floor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='apartment', to='apartments.floorplan'),
        ),
        migrations.AlterField(
            model_name='apartmentssale',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'For Sale'), (2, 'Booked'), (3, 'Sold')], default=1),
        ),
        migrations.AlterField(
            model_name='explication',
            name='layout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='explication', to='apartments.layout'),
        ),
        migrations.AlterField(
            model_name='floorplan',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='floorplan', to='apartments.section'),
        ),
        migrations.AlterField(
            model_name='layout',
            name='image',
            field=models.ImageField(null=True, upload_to='photo_layout/%Y/%m/%d'),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]