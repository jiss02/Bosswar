# Generated by Django 2.2.3 on 2019-07-17 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_profile_votes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]