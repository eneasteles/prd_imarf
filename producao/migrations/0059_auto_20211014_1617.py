# Generated by Django 3.2.4 on 2021-10-14 19:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0058_auto_20211014_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resina_valor',
            name='data_compra',
            field=models.DateField(default=datetime.datetime(2021, 10, 14, 19, 17, 50, 21325, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='resinamento',
            name='data',
            field=models.DateField(default=datetime.datetime(2021, 10, 14, 19, 17, 50, 22324, tzinfo=utc)),
        ),
    ]
