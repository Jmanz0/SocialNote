# Generated by Django 4.1 on 2022-08-25 14:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0002_alter_note_description_alter_note_tag_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="time",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 25, 14, 59, 3, 612515)
            ),
        ),
    ]