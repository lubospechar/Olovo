# Generated by Django 5.1.1 on 2024-11-28 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dbolovo", "0006_alter_sample_options_remove_sample_name_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Sample",
            new_name="CollectedSample",
        ),
    ]