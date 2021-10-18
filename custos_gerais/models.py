from django.db import models
from producao.models import *

# Create your models here.
class Item_de_Producao(models.Model):
    #id = models.AutoField(primary_key=True)
    item_de_producao = models.CharField(max_length=100, default='indefinido')
    def __str__(self):
        return self.item_de_producao

class Custo_Geral(models.Model):
    #id = models.AutoField(primary_key=True)    
    ano = models.IntegerField(default=timezone.now().year)
    mes = models.IntegerField(choices=MES_CHOICES)
    producao_m2 = models.FloatField()    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.ano) + ' - ' + str(self.mes)

class Custo_Geral_Item(models.Model):
    custo_geral_id = models.ForeignKey(Custo_Geral, on_delete=PROTECT)
    item_de_producao_id = models.ForeignKey(Item_de_Producao, on_delete=PROTECT, default=1)
    quantidade = models.FloatField(default=0)
    unidade = models.ForeignKey(Unidade, on_delete=PROTECT, default=1)
    valor = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Energia(models.Model):
    ano = models.IntegerField(default=timezone.now().year)
    mes = models.IntegerField(choices=MES_CHOICES)
    consumo_hp = models.DecimalField(max_digits=12, decimal_places=2, default=0)  
    consumo_hfp = models.DecimalField(max_digits=12, decimal_places=2, default=0) 
    valor = models.DecimalField(max_digits=12, decimal_places=2, default=0)  
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return str(self.ano) + ' - ' + str(self.mes)
