from django.db import models
from django.db.models.fields import CharField
from producao.models import Centro_de_Custo

# Create your models here.


class Cadastro_Funcionario(models.Model):
    nome = models.CharField(max_length=100)    
    cpf = models.CharField(max_length=15, blank=True, null=True)
    centro_de_custo = models.ForeignKey(Centro_de_Custo, on_delete=models.CASCADE, default=4)
    folha = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    produtividade = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    outros = models.DecimalField(max_digits=10, decimal_places=2, default=0)    
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Resumo_Funcionarios_View(models.Model):
    centro_de_custo = CharField(max_length=100, primary_key=True)
    qtde_funcionarios = models.IntegerField(default=0)
    folha = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    produtividade = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    outros = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    valor = models.DecimalField(max_digits=14, decimal_places=2, default=0)

    class Meta:
        managed=False
        db_table='resumo_funcionarios_view'