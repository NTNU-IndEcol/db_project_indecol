# Generated by Django 4.2.6 on 2023-10-25 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_indecol", "0003_person"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="role",
            field=models.CharField(
                choices=[
                    ("M", "Master Student"),
                    ("PhD", "PhD"),
                    ("PD", "PostDoc"),
                    ("E", "Enginner"),
                    ("AP", "Associate Professor"),
                    ("R", "Researcher"),
                    ("P", "Professor"),
                ],
                max_length=50,
            ),
        ),
    ]