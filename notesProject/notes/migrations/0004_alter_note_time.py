# Generated by Django 4.1 on 2022-08-25 14:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0003_alter_note_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="time",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 8, 25, 14, 59, 10, 798584)
            ),
        ),
    ]