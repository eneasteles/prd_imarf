# Generated by Django 3.2.4 on 2021-08-23 12:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0017_alter_resinamento_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resinamento',
            name='data',
            field=models.DateField(default=datetime.datetime(2021, 8, 23, 12, 14, 4, 85933, tzinfo=utc)),
        ),
    ]
