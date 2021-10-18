# Generated by Django 3.2.4 on 2021-09-29 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setor_pessoal', '0005_cadastro_funcionario_cpf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resumo_Funcionarios_View',
            fields=[
                ('centro_de_custo', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('qtde_funcionarios', models.IntegerField(default=0)),
                ('folha', models.DecimalField(decimal_places=2, default=0, max_digits=14)),
                ('produtividade', models.DecimalField(decimal_places=2, default=0, max_digits=14)),
                ('outros', models.DecimalField(decimal_places=2, default=0, max_digits=14)),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=14)),
            ],
            options={
                'db_table': 'resumo_funcionarios_view',
                'managed': False,
            },
        ),
        migrations.RenameField(
            model_name='cadastro_funcionario',
            old_name='Centro_de_Custo',
            new_name='centro_de_custo',
        ),
    ]
