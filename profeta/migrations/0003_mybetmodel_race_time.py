# Generated by Django 3.2.8 on 2021-11-01 13:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profeta', '0002_auto_20211101_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='mybetmodel',
            name='race_time',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)]),
        ),
    ]
