# Generated by Django 4.0.2 on 2022-06-21 08:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0021_auto_20220614_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='helicopter_avg_fuel_consumption',
            field=models.FloatField(
                help_text='Helicopter average fuel consumption (t/d)',
                validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(120)],
            ),
        ),
        migrations.AlterField(
            model_name='project',
            name='nox_tax',
            field=models.PositiveIntegerField(
                help_text='NOX tax (USD/t)',
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(10000),
                ],
            ),
        ),
    ]
