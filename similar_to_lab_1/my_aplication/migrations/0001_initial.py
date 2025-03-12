# Generated by Django 5.1.7 on 2025-03-12 16:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Manufacturer",
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
                ("name", models.CharField(max_length=50)),
                ("web_site", models.URLField()),
                ("country", models.CharField(max_length=50)),
                ("owner", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Workplace",
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
                ("name", models.CharField(max_length=50)),
                ("year_founded", models.IntegerField()),
                ("repairs_oldTimers", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Vehicle",
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
                ("vehicle_type", models.CharField(max_length=70)),
                ("max_speed", models.IntegerField()),
                ("color", models.CharField(max_length=30)),
                (
                    "manufacturer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="my_aplication.manufacturer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Repairment",
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
                ("code", models.CharField(max_length=8, unique=True)),
                ("application_date", models.DateField()),
                ("description_of_problem", models.TextField()),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="repairments/"),
                ),
                (
                    "user_reported",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "vehicle",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="my_aplication.vehicle",
                    ),
                ),
                (
                    "workplace",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="my_aplication.workplace",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="WorkplaceForManufacturers",
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
                    "manufacturer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="my_aplication.manufacturer",
                    ),
                ),
                (
                    "workplace",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="my_aplication.workplace",
                    ),
                ),
            ],
        ),
    ]
