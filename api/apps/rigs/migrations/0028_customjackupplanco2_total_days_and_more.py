# Generated by Django 4.0.2 on 2022-10-06 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rigs', '0027_alter_customjackupplanco2_cost_per_meter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customjackupplanco2',
            name='total_days',
            field=models.FloatField(blank=True, default=0, help_text='Total days', null=True),
        ),
        migrations.AddField(
            model_name='customsemiplanco2',
            name='total_days',
            field=models.FloatField(blank=True, default=0, help_text='Total days', null=True),
        ),
    ]