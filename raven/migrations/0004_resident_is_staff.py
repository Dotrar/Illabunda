# Generated by Django 3.2.8 on 2021-11-01 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raven', '0003_auto_20211101_0739'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
