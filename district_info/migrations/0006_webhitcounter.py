# Generated by Django 3.0.4 on 2020-04-15 13:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('district_info', '0005_auto_20200415_1937'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebHitCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name=datetime.datetime(2020, 4, 15, 19, 55, 12, 128993))),
                ('counter', models.PositiveIntegerField()),
            ],
        ),
    ]
