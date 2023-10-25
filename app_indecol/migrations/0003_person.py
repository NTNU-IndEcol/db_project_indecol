# Generated by Django 4.2.6 on 2023-10-25 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_indecol", "0002_alter_project_end_date_alter_project_keywords_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Person",
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
                ("person_id", models.CharField(max_length=50, unique=True)),
                ("first_name", models.CharField(max_length=50)),
                ("middle_name", models.CharField(blank=True, max_length=50, null=True)),
                ("last_name", models.CharField(max_length=50)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                ("role", models.CharField(max_length=50)),
            ],
        ),
    ]