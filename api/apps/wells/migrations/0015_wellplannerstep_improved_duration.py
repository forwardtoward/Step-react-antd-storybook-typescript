# Generated by Django 4.0.2 on 2022-08-02 10:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0014_merge_20220726_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='wellplannerstep',
            name='improved_duration',
            field=models.FloatField(
                default=0,
                help_text='Phase improved duration in days',
                validators=[django.core.validators.MinValueValidator(0)],
            ),
            preserve_default=False,
        ),
    ]