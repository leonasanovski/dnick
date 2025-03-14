# Generated by Django 5.1.7 on 2025-03-10 22:30

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
            name="Balloon",
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
                    "balloon_type",
                    models.CharField(
                        choices=[("L", "Large"), ("M", "Medium"), ("S", "Small")],
                        max_length=1,
                    ),
                ),
                ("manufacturer", models.CharField(max_length=100)),
                ("maximum_capacity", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="FlightCompany",
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
                ("company_name", models.CharField(max_length=100)),
                ("year_of_establishment", models.IntegerField()),
                ("is_europe_only", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Pilot",
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
                ("name", models.CharField(max_length=100)),
                ("surname", models.CharField(max_length=100)),
                ("year_of_birth", models.IntegerField()),
                (
                    "total_hours_on_flight",
                    models.DecimalField(decimal_places=1, max_digits=5),
                ),
                (
                    "rank_in_company",
                    models.CharField(
                        choices=[
                            ("B", "Beginner"),
                            ("I", "Intermediate"),
                            ("E", "Expert"),
                        ],
                        max_length=1,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Flight",
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
                ("code", models.CharField(max_length=10, unique=True)),
                ("departure_airport", models.CharField(max_length=50, unique=True)),
                ("landing_airport", models.CharField(max_length=50, unique=True)),
                (
                    "flight_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="flight_images/"
                    ),
                ),
                (
                    "balloon",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.balloon"
                    ),
                ),
                (
                    "user_that_created",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "flight_company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.flightcompany",
                    ),
                ),
                (
                    "pilot",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.pilot"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AirCompanyPilot",
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
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.flightcompany",
                    ),
                ),
                (
                    "pilot",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.pilot"
                    ),
                ),
            ],
        ),
    ]
