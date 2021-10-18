# Generated by Django 3.2.4 on 2021-09-28 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producao', '0050_alter_resinamento_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Produto',
            fields=[
                ('tipo', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.FloatField()),
                ('comprimento', models.DecimalField(decimal_places=3, max_digits=6)),
                ('altura_espessura', models.DecimalField(decimal_places=3, max_digits=6)),
                ('largura', models.DecimalField(decimal_places=3, max_digits=6)),
                ('preco', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('acabamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.acabamento')),
                ('detalhe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.detalhe')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.material')),
                ('qualidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.qualidade')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='estoque.tipo_produto')),
                ('unidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.un')),
            ],
        ),
    ]
