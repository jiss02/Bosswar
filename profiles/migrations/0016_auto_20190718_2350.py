# Generated by Django 2.2.3 on 2019-07-18 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_auto_20190718_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='point',
            field=models.IntegerField(default=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='votes',
            field=models.IntegerField(default=2),
        ),
    ]
