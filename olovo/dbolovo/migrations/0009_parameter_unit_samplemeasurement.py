# Generated by Django 5.1.1 on 2024-11-28 14:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dbolovo", "0008_collectedsample_identifier"),
    ]

    operations = [
        migrations.CreateModel(
            name="Parameter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Zadejte název měřeného parametru, například pH nebo obsah těžkých kovů",
                        max_length=100,
                        unique=True,
                        verbose_name="Název parametru",
                    ),
                ),
            ],
            options={
                "verbose_name": "Parametr",
                "verbose_name_plural": "Parametry",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Unit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Zadejte jednotku měření, například mg/l nebo pH",
                        max_length=50,
                        unique=True,
                        verbose_name="Jednotka",
                    ),
                ),
            ],
            options={
                "verbose_name": "Jednotka",
                "verbose_name_plural": "Jednotky",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="SampleMeasurement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "value",
                    models.FloatField(
                        help_text="Zadejte naměřenou hodnotu parametru",
                        verbose_name="Hodnota",
                    ),
                ),
                (
                    "parameter",
                    models.ForeignKey(
                        help_text="Vyberte měřený parametr",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dbolovo.parameter",
                        verbose_name="Parametr",
                    ),
                ),
                (
                    "sample",
                    models.ForeignKey(
                        help_text="Vyberte vzorek, ke kterému tato měření patří",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="measurements",
                        to="dbolovo.collectedsample",
                        verbose_name="Vzorek",
                    ),
                ),
                (
                    "unit",
                    models.ForeignKey(
                        help_text="Vyberte jednotku měření",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dbolovo.unit",
                        verbose_name="Jednotka",
                    ),
                ),
            ],
            options={
                "verbose_name": "Měření vzorku",
                "verbose_name_plural": "Měření vzorků",
                "ordering": ["sample", "parameter"],
            },
        ),
    ]
