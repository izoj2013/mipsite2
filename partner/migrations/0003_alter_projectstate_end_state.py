# Generated by Django 4.0.2 on 2022-02-17 07:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0002_alter_projectstate_end_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectstate',
            name='end_state',
            field=models.DateField(default=datetime.datetime(2022, 8, 17, 7, 23, 14, 264559)),
        ),
    ]
