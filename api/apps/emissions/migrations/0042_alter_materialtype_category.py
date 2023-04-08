# Generated by Django 4.0.2 on 2022-11-09 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emissions', '0041_merge_20221108_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialtype',
            name='category',
            field=models.CharField(
                choices=[('STEEL', 'Steel'), ('CEMENT', 'Cement'), ('BULK', 'Bulk'), ('CHEMICALS', 'Chemicals')],
                max_length=64,
            ),
        ),
    ]
