# Generated by Django 5.1.1 on 2024-10-07 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dbolovo", "0005_sample_delete_location"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="sample",
            options={
                "ordering": ["location_name", "year"],
                "verbose_name": "Vzorek",
                "verbose_name_plural": "Vzorky",
            },
        ),
        migrations.RemoveField(
            model_name="sample",
            name="name",
        ),
        migrations.AddField(
            model_name="sample",
            name="location_name",
            field=models.CharField(
                default=1,
                help_text="Zadejte název lokality, kde byl vzorek odebrán",
                max_length=200,
                verbose_name="Název lokality",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="sample",
            name="year",
            field=models.IntegerField(
                help_text="Rok, kdy byl vzorek odebrán", verbose_name="Rok"
            ),
        ),
    ]