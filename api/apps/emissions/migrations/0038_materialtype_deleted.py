# Generated by Django 4.0.2 on 2022-11-07 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emissions', '0037_merge_20221107_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialtype',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]