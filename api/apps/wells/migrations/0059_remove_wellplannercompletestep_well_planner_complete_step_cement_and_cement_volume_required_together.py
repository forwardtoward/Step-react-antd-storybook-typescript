# Generated by Django 4.0.2 on 2022-11-29 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wells', '0058_auto_20221129_1219'),
    ]

    state_operations = [
        migrations.RemoveConstraint(
            model_name='wellplannercompletestep',
            name='well_planner_complete_step_cement_and_cement_volume_required_together',
        ),
        migrations.RemoveConstraint(
            model_name='wellplannercompletestep',
            name='well_planner_complete_step_steel_and_steel_weight_required_together',
        ),
        migrations.RemoveConstraint(
            model_name='wellplannerplannedstep',
            name='well_planner_planned_step_cement_and_cement_volume_required_together',
        ),
        migrations.RemoveConstraint(
            model_name='wellplannerplannedstep',
            name='well_planner_planned_step_steel_and_steel_weight_required_together',
        ),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=state_operations,
        ),
        migrations.RemoveField(
            model_name='wellplannercompletestep',
            name='carbon_capture_storage_system',
        ),
        migrations.RemoveField(
            model_name='wellplannercompletestep',
            name='cement',
        ),
        migrations.RemoveField(
            model_name='wellplannercompletestep',
            name='cement_volume',
        ),
        migrations.RemoveField(
            model_name='wellplannercompletestep',
            name='external_energy_supply',
        ),
        migrations.RemoveField(
            model_name='wellplannercompletestep',
            name='steel',
        ),
        migrations.RemoveField(
            model_name='wellplannercompletestep',
            name='steel_weight',
        ),
        migrations.RemoveField(
            model_name='wellplannerplannedstep',
            name='carbon_capture_storage_system',
        ),
        migrations.RemoveField(
            model_name='wellplannerplannedstep',
            name='cement',
        ),
        migrations.RemoveField(
            model_name='wellplannerplannedstep',
            name='cement_volume',
        ),
        migrations.RemoveField(
            model_name='wellplannerplannedstep',
            name='external_energy_supply',
        ),
        migrations.RemoveField(
            model_name='wellplannerplannedstep',
            name='steel',
        ),
        migrations.RemoveField(
            model_name='wellplannerplannedstep',
            name='steel_weight',
        ),
    ]