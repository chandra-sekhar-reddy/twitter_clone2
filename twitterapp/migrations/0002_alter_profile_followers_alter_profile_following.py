# Generated by Django 4.2.1 on 2023-05-23 20:17

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitterapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='followers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=list, max_length=255), size=None),
        ),
        migrations.AlterField(
            model_name='profile',
            name='following',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=list, max_length=255), size=None),
        ),
    ]