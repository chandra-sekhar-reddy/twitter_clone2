# Generated by Django 4.2.1 on 2023-05-24 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitterapp', '0004_profile_followingtweet_profile_tweet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='followingtweet',
        ),
    ]