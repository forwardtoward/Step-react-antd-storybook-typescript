# Generated by Django 4.0.2 on 2022-10-04 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0041_alter_wellplanner_baseline'),
    ]

    database_operations = [migrations.AlterModelTable('wellplannerphase', 'emissions_wellplannerphase')]

    operations = [migrations.SeparateDatabaseAndState(database_operations=database_operations, state_operations=[])]
