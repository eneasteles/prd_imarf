# Generated by Django 3.2.4 on 2021-08-31 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polimento', '0003_auto_20210824_1555'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jogo_de_abrasivos',
            options={},
        ),
        migrations.RenameField(
            model_name='jogo_de_abrasivos',
            old_name='data_cadastro',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='jogo_de_abrasivos',
            old_name='data_alteracao',
            new_name='updated',
        ),
        migrations.RemoveField(
            model_name='jogo_de_abrasivos',
            name='abr',
        ),
        migrations.RemoveField(
            model_name='jogo_de_abrasivos',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='jogo_de_abrasivos',
            name='fornecedor',
        ),
        migrations.RemoveField(
            model_name='jogo_de_abrasivos',
            name='grao',
        ),
        migrations.RemoveField(
            model_name='jogo_de_abrasivos',
            name='tipo',
        ),
        migrations.AddField(
            model_name='jogo_de_abrasivos',
            name='abrasivo_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='polimento.abrasivo'),
        ),
        migrations.AddField(
            model_name='jogo_de_abrasivos',
            name='cabeca',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='jogo_de_abrasivos',
            name='data',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='jogo_de_abrasivos',
            name='polimento_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='polimento.polimento'),
        ),
        migrations.AddField(
            model_name='jogo_de_abrasivos',
            name='quantidade',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='abrasivo',
            name='usuario_cadastrou',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
