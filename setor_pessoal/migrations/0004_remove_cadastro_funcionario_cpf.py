# Generated by Django 3.2.4 on 2021-09-28 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setor_pessoal', '0003_cadastro_funcionario_centro_de_custo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadastro_funcionario',
            name='cpf',
        ),
    ]
