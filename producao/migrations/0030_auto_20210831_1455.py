# Generated by Django 3.2.4 on 2021-08-31 17:55

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0029_auto_20210825_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resinamento',
            name='data',
            field=models.DateField(default=datetime.datetime(2021, 8, 31, 17, 55, 22, 485834, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='resinamento_item',
            name='resinamento_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.resinamento', verbose_name='Insumo'),
        ),
    ]
