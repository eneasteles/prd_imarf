# Generated by Django 3.2.4 on 2021-09-28 14:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0051_alter_resinamento_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resinamento',
            name='data',
            field=models.DateField(default=datetime.datetime(2021, 9, 28, 14, 49, 7, 23528, tzinfo=utc)),
        ),
    ]