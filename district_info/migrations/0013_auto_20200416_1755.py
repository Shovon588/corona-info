# Generated by Django 3.0.4 on 2020-04-16 11:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('district_info', '0012_auto_20200416_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='divisioninfo',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 4, 16, 17, 55, 18, 521040)),
        ),
        migrations.AlterField(
            model_name='webhitcounter',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 17, 55, 18, 521711)),
        ),
    ]
