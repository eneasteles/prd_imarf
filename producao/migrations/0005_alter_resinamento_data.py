# Generated by Django 3.2.4 on 2021-08-23 12:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0004_alter_resinamento_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resinamento',
            name='data',
            field=models.DateField(default=datetime.datetime(2021, 8, 23, 12, 7, 52, 513147, tzinfo=utc)),
        ),
    ]
