# Generated by Django 3.0.4 on 2020-04-15 14:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('district_info', '0006_webhitcounter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webhitcounter',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 15, 20, 1, 41, 553227)),
        ),
    ]