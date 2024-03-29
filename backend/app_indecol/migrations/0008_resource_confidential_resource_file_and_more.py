# Generated by Django 4.2.6 on 2024-03-20 11:18

import app_indecol.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_indecol', '0007_alter_team_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='confidential',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='resource',
            name='file',
            field=models.FileField(null=True, upload_to=app_indecol.models.resource_path),
        ),
        migrations.AlterField(
            model_name='resource',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
    ]
