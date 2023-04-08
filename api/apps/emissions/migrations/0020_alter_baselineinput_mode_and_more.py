# Generated by Django 4.0.2 on 2022-10-05 09:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emissions', '0019_rename_wellplannermode_custommode'),
    ]

    state_operations = [
        migrations.AlterField(
            model_name='baselineinput',
            name='mode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='emissions.custommode'),
        ),
        migrations.AlterField(
            model_name='customempinitiativephase',
            name='mode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='emissions.custommode'),
        ),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(state_operations=state_operations),
        migrations.AlterField(
            model_name='custommode',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='emissions.asset'),
        ),
    ]
