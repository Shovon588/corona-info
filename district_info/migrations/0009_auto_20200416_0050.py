# Generated by Django 3.0.4 on 2020-04-15 18:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('district_info', '0008_auto_20200415_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caseinfo',
            name='date',
            field=models.DateField(default=datetime.date(2020, 4, 16)),
        ),
        migrations.AlterField(
            model_name='totalinfo',
            name='date',
            field=models.DateField(default=datetime.date(2020, 4, 16)),
        ),
        migrations.AlterField(
            model_name='webhitcounter',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 0, 50, 8, 371396)),
        ),
    ]
