# Generated by Django 5.0.2 on 2024-02-22 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_vaccins', '0002_rename_nucd_ods_flux_total_dep_nb_ucd'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ods_flux_total_dep',
            old_name='nb_dose',
            new_name='nb_doses',
        ),
    ]
