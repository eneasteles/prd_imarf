# Generated by Django 3.2.4 on 2021-09-28 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setor_pessoal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro_funcionario',
            name='outros',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='cadastro_funcionario',
            name='produtividade',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
