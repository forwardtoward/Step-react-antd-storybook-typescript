# Generated by Django 4.0.2 on 2022-07-21 08:57

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0008_auto_20220324_1446'),
        ('rigs', '0025_alter_conceptdrillship_hull_depth_and_more'),
        ('projects', '0026_auto_20220630_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConceptCarbonCaptureStorageSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('co2', models.FloatField(help_text='CO2 emission per day in mT')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tenants.tenant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ConceptCement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('co2', models.FloatField(help_text='CO2 emission per m3 of cement in tons')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tenants.tenant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ConceptExternalSupply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('energy', models.FloatField(help_text='Available energy per day in Mw')),
                ('co2', models.FloatField(help_text='Daily CO2 emission per Kw/h in tons')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tenants.tenant')),
            ],
            options={
                'verbose_name': 'Concept External Supply',
                'verbose_name_plural': 'Concept External Supplies',
            },
        ),
        migrations.CreateModel(
            name='ConceptHelicopter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('fuel', models.FloatField(help_text='Helicopter fuel consumption per hour in liters')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tenants.tenant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ConceptSteel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('co2', models.FloatField(help_text='CO2 emission per ton of steel in tons')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tenants.tenant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ConceptVessel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('fuel_summer', models.FloatField(help_text='Summer daily fuel consumption in cubic meters')),
                ('fuel_winter', models.FloatField(help_text='Winter daily fuel consumption in cubic meters')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tenants.tenant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RigPlanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                (
                    'custom_drillship',
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='rigs.customdrillship'
                    ),
                ),
                (
                    'custom_jackup_rig',
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='rigs.customjackuprig'
                    ),
                ),
                (
                    'custom_semi_rig',
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='rigs.customsemirig'
                    ),
                ),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tenants.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='CustomVessel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                (
                    'fuel_summer',
                    models.FloatField(
                        help_text='Summer daily fuel consumption in cubic meters',
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    'fuel_winter',
                    models.FloatField(
                        help_text='Winter daily fuel consumption in cubic meters',
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    'rig_planner',
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.rigplanner'),
                ),
                ('vessel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.conceptvessel')),
            ],
        ),
        migrations.CreateModel(
            name='CustomSteel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                (
                    'co2',
                    models.FloatField(
                        help_text='CO2 emission per ton of steel in tons',
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    'rig_planner',
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.rigplanner'),
                ),
                ('steel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.conceptsteel')),
            ],
        ),
        migrations.CreateModel(
            name='CustomHelicopter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                (
                    'fuel',
                    models.FloatField(
                        help_text='Fuel consumption per hour in liters',
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    'helicopter',
                    models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.concepthelicopter'),
                ),
                (
                    'rig_planner',
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.rigplanner'),
                ),
            ],
        ),
        migrations.CreateModel(
            name='CustomExternalSupply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                (
                    'energy',
                    models.FloatField(
                        help_text='Available energy per day in Kw/h',
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    'co2',
                    models.FloatField(
                        help_text='Daily CO2 emission per Kw/h in tons',
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    'external_supply',
                    models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.conceptexternalsupply'),
                ),
                (
                    'rig_planner',
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.rigplanner'),
                ),
            ],
            options={
                'verbose_name': 'Custom External Supply',
                'verbose_name_plural': 'Custom External Supplies',
            },
        ),
        migrations.CreateModel(
            name='CustomCement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                (
                    'co2',
                    models.FloatField(
                        help_text='CO2 emission per cubic meter of cement in tons',
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                ('cement', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.conceptcement')),
                (
                    'rig_planner',
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.rigplanner'),
                ),
            ],
        ),
        migrations.CreateModel(
            name='CustomCarbonCaptureStorageSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                (
                    'co2',
                    models.FloatField(
                        help_text='CO2 emission per day in mT', validators=[django.core.validators.MinValueValidator(0)]
                    ),
                ),
                (
                    'carbon_capture_storage_system',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to='projects.conceptcarboncapturestoragesystem'
                    ),
                ),
                (
                    'rig_planner',
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.rigplanner'),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name='rigplanner',
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(
                        ('custom_jackup_rig__isnull', False),
                        ('custom_semi_rig__isnull', True),
                        ('custom_drillship', True),
                    ),
                    models.Q(
                        ('custom_jackup_rig', True), ('custom_semi_rig__isnull', False), ('custom_drillship', True)
                    ),
                    models.Q(
                        ('custom_jackup_rig', True), ('custom_semi_rig__isnull', True), ('custom_drillship', False)
                    ),
                    _connector='OR',
                ),
                name='single_rig_planner_rig',
            ),
        ),
        migrations.AlterUniqueTogether(
            name='customvessel',
            unique_together={('rig_planner', 'vessel')},
        ),
        migrations.AlterUniqueTogether(
            name='customsteel',
            unique_together={('rig_planner', 'steel')},
        ),
        migrations.AlterUniqueTogether(
            name='customhelicopter',
            unique_together={('rig_planner', 'helicopter')},
        ),
        migrations.AlterUniqueTogether(
            name='customexternalsupply',
            unique_together={('rig_planner', 'external_supply')},
        ),
        migrations.AlterUniqueTogether(
            name='customcement',
            unique_together={('rig_planner', 'cement')},
        ),
        migrations.AlterUniqueTogether(
            name='customcarboncapturestoragesystem',
            unique_together={('rig_planner', 'carbon_capture_storage_system')},
        ),
    ]
