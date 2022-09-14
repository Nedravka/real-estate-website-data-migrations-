# Generated by Django 2.2.24 on 2022-08-30 20:02

from django.db import migrations


def parse_owners_info(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats = Flat.objects.all().values('owner', 'owners_phonenumber', 'owner_pure_phone')
    for flat in flats.iterator():
        Owner.objects.get_or_create(name=flat['owner'], phonenumber=flat['owners_phonenumber'], pure_phonenumber=flat['owner_pure_phone'])


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_owner'),
    ]

    operations = [
        migrations.RunPython(parse_owners_info)
    ]
