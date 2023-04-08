# Generated by Django 4.0.2 on 2022-10-13 10:25

from django.db import migrations


def migrate_helicopter_name(apps, *args):
    CustomHelicopter = apps.get_model('projects', 'CustomHelicopter')

    for custom_helicopter in CustomHelicopter.objects.all():
        custom_helicopter.name = custom_helicopter.helicopter.name
        custom_helicopter.save()


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0039_customhelicopter_name'),
    ]

    operations = [migrations.RunPython(migrate_helicopter_name)]