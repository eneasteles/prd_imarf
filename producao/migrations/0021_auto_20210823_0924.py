# Generated by Django 3.2.4 on 2021-08-23 12:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0020_auto_20210823_0922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resinamento',
            name='quantidade_de_chapas',
        ),
        migrations.AlterField(
            model_name='resinamento',
            name='data',
            field=models.DateField(default=datetime.datetime(2021, 8, 23, 12, 24, 9, 536721, tzinfo=utc)),
        ),
    ]