# Generated by Django 5.1.1 on 2024-11-28 14:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dbolovo", "0009_parameter_unit_samplemeasurement"),
    ]

    operations = [
        migrations.AlterField(
            model_name="samplemeasurement",
            name="unit",
            field=models.ForeignKey(
                blank=True,
                help_text="Vyberte jednotku měření",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="dbolovo.unit",
                verbose_name="Jednotka",
            ),
        ),
    ]
