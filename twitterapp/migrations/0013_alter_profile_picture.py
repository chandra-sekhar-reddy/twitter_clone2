# Generated by Django 4.2.1 on 2023-05-29 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitterapp', '0012_alter_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='twitterlogo.png', upload_to='images/'),
        ),
    ]