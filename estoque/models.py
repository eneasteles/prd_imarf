from django.db import models
from producao.models import *

# Create your models here.
class Tipo_Produto(models.Model):
    tipo = models.CharField(max_length=50, primary_key=True)
    def __str__(self):
        return self.tipo

class Estoque(models.Model):
    material = models.ForeignKey(Material, on_delete=PROTECT)
    tipo = models.ForeignKey(Tipo_Produto, on_delete=PROTECT)
    acabamento = models.ForeignKey(Acabamento, on_delete=PROTECT)
    qualidade = models.ForeignKey(Qualidade, on_delete=PROTECT)
    detalhe = models.ForeignKey(Detalhe, on_delete=PROTECT)
    quantidade = models.FloatField()
    unidade = models.ForeignKey(Un, on_delete=PROTECT)
    comprimento = DecimalField(max_digits=6, decimal_places=3)
    altura_espessura = DecimalField(max_digits=6, decimal_places=3)
    largura = DecimalField(max_digits=6, decimal_places=3)
    preco = models.FloatField()    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.material)