# Generated by Django 4.0.2 on 2022-10-24 11:42

from django.db import migrations


def create_default_external_energy_supply(apps, *args):
    ExternalEnergySupply = apps.get_model('emissions', 'ExternalEnergySupply')
    Asset = apps.get_model('emissions', 'Asset')

    for asset in Asset.objects.all():
        ExternalEnergySupply.objects.get_or_create(
            asset=asset,
            defaults={
                'type': 'External Energy Supply',
                'capacity': 0,
                'co2': 0,
                'nox': 0,
                'generator_efficiency_factor': 0,
            },
        )


class Migration(migrations.Migration):

    dependencies = [('emissions', '0032_merge_20221024_1139'), ('projects', '0057_delete_externalenergysupply')]

    operations = [migrations.RunPython(create_default_external_energy_supply)]
