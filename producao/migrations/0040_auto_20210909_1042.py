# Generated by Django 3.2.4 on 2021-09-09 13:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0039_alter_resinamento_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedido_venda_item',
            options={'verbose_name': 'Item', 'verbose_name_plural': 'Itens do Pedido'},
        ),
        migrations.AddField(
            model_name='pedido_venda',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AddField(
            model_name='pedido_venda_item',
            name='preco',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='pedido_venda_item',
            name='valor',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='resinamento',
            name='data',
            field=models.DateField(default=datetime.datetime(2021, 9, 9, 13, 42, 12, 88280, tzinfo=utc)),
        ),
    ]
