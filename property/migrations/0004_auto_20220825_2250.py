# Generated by Django 2.2.24 on 2022-08-25 18:50

from django.db import migrations


def make_buildings_new(apps, schema_editor):
    Flat = apps.get_model('property', 'FLat')
    for flat in Flat.objects.all():
        if flat.construction_year >= 2015:
            flat.is_new_building = True
        else:
            flat.is_new_building = False
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_is_new_building'),
    ]

    operations = [
        migrations.RunPython(make_buildings_new)
    ]
