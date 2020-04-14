# Generated by Django 3.0.4 on 2020-04-14 06:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('district_info', '0003_auto_20200413_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='DivisionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cases', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='caseinfo',
            name='date',
            field=models.DateField(default=datetime.date(2020, 4, 14)),
        ),
        migrations.AlterField(
            model_name='totalinfo',
            name='date',
            field=models.DateField(default=datetime.date(2020, 4, 14)),
        ),
    ]
