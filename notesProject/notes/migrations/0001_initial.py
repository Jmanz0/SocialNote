# Generated by Django 4.1 on 2022-08-24 16:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Note",
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
                ("title", models.CharField(max_length=100, null=True)),
                ("description", models.CharField(max_length=1000, null=True)),
                (
                    "time",
                    models.DateTimeField(
                        default=datetime.datetime(2022, 8, 24, 16, 2, 37, 752088)
                    ),
                ),
                ("tag", models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
