# Generated by Django 4.0.2 on 2022-06-09 11:20

from django.db import migrations


def add_reference_rigs(apps, *args):
    Plan = apps.get_model("projects", "Plan")

    for plan in Plan.objects.select_related('project'):
        jackup_rig = plan.project.jackup_rigs.filter(draft=False).first()
        if jackup_rig:
            plan.reference_operation_jackup = jackup_rig
            plan.save()
            continue

        semi_rig = plan.project.semi_rigs.filter(draft=False).first()
        if semi_rig:
            plan.reference_operation_semi = semi_rig
            plan.save()
            continue

        drillship = plan.project.drillships.filter(draft=False).first()
        if drillship:
            plan.reference_operation_drillship = drillship
            plan.save()
            continue

        plan.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_rename_operation_end_date_plan_reference_operation_end_date_and_more'),
    ]

    operations = [migrations.RunPython(add_reference_rigs)]