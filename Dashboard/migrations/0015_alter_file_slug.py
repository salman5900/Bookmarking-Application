# Generated by Django 5.2.1 on 2025-05-12 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0014_file_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
