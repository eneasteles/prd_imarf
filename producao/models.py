from datetime import date, datetime
from django.conf.urls import url
from django.contrib.admin.sites import DefaultAdminSite
from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.db.models.fields import CharField, DecimalField
from django.db.models.fields.related import ForeignKey
from django.utils.regex_helper import Group
from django.utils import timezone
from django.utils.tree import Node
from django.contrib.auth.models import User
from serraria.models import *
#from django_pgviews import view as pg

MES_CHOICES = (
        (1,'JANEIRO'),
        (2,'FEVEREIRO'),
        (3,'MARÇO'),
        (4,'ABRIL'),
        (5,'MAIO'),
        (6,'JUNHO'),
        (7,'JULHO'),
        (8,'AGOSTO'),
        (9,'SETEMBRO'),
        (10,'OUTUBRO'),
        (11,'NOVEMBRO'),
        (12,'DEZEMBRO')
    )

LINHA_CHOICES = (
        ('1', 'MESAS'),
        ('2', 'AUTOMÁTICA'),
        ('3', 'AUTOMÁTICA C/30 BANDEIJAS')
    )
class Unidade_de_Medida(models.Model):
    unidade = models.CharField(max_length=30, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.unidade)
class Centro_de_Custo(models.Model):
    centro_de_custo = models.CharField(max_length=100)

    def __str__(self):
        return str(self.centro_de_custo)
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cnpjcpf = models.CharField(max_length=14)

    def __str__(self):
        return str(self.nome)

class Pedreira(models.Model):
    pedreira = CharField(max_length=100)
    cidade = CharField(max_length=100, blank=True, null=True)
    centro_de_custo = models.ForeignKey(Centro_de_Custo, on_delete=PROTECT, default=1)
    usuario = models.ForeignKey(User, default=1 ,on_delete=PROTECT)

    
    def __str__(self):
        return str(self.pedreira)

class Material(models.Model):
    material = models.CharField(max_length=100)
    dureza = models.IntegerField(default= True) 
    pedreira = models.ForeignKey(Pedreira, on_delete=PROTECT, default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.material

class Status_bloco(models.Model):
    status = models.CharField(max_length=15)

    def __str__(self):
        return self.status

class Bloco(models.Model):
    TIPO_CHOICES = (
        ('A','PRIMEIRA'),
        ('B','SEGUNDA LINHA')
    )
    bloco = models.CharField(max_length=15)
    material = models.ForeignKey(Material, on_delete=models.PROTECT) 
    tipo = models.CharField(max_length=1, default='A', choices=TIPO_CHOICES)   
    comprimento = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    altura = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    largura = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    status = models.ForeignKey(Status_bloco, on_delete=models.PROTECT) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, default=3, on_delete=PROTECT)



    def __str__(self):
        return self.bloco

class Espessura(models.Model):
    espessura = models.DecimalField(max_digits=6, decimal_places=3, default=0.02, primary_key=True)

    def __str__(self):
        return str(self.espessura)


class Status_chapa(models.Model):
    status = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.status

class Acabamento(models.Model):
    acabamento = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.acabamento

class Observacao_chapa(models.Model):
    observacao_chapa = models.CharField(max_length=100)

    def __str__(self):
        return self.observacao_chapa

class Chapa(models.Model):
    chapa = models.IntegerField()
    bloco = models.ForeignKey(Bloco, on_delete=models.PROTECT)
    acabamento = models.ForeignKey(Acabamento, on_delete=PROTECT)
    espessura = models.ForeignKey(Espessura, on_delete=models.PROTECT)
    observacao_chapa = models.ForeignKey(Observacao_chapa, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.chapa)

class Insumo(models.Model):
    insumo = models.CharField(max_length=100)

    def __str__(self):
        return str(self.insumo)

class Unidade(models.Model):
    unidade = models.CharField(max_length=20)
    fator = models.DecimalField(max_digits=10, decimal_places=3, default=1)
    descricao_unidade = models.CharField(max_length=100, default='')

    def __str__(self):
        return str(self.unidade)

class Un(models.Model):
    unidade = models.CharField(max_length=20, primary_key=True)
    fator = models.DecimalField(max_digits=10, decimal_places=3, default=1)
    descricao_unidade = models.CharField(max_length=100, default='')

    def __str__(self):
        return str(self.unidade)

class Maquina(models.Model):
    maquina = models.CharField(max_length=100)
    lacada = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.maquina)

  

class Liga(models.Model):
    liga = models.CharField(max_length=25)
    
    def __str__(self):
        return str(self.liga)

class Fio_diamantado(models.Model):
    jogo_fio= models.IntegerField(primary_key=True)
    maquina = models.ForeignKey(Maquina, on_delete=PROTECT)
    espessura_fio = models.DecimalField(max_digits=6, decimal_places=3)
    referencia = models.CharField(max_length=50, blank=True)
    nome = models.ForeignKey(Pessoa, on_delete=PROTECT)
    nota_fiscal = models.IntegerField()
    status_fio = models.CharField(max_length=1,default='A', choices=(('A','ATIVO'),('F','FINALIZADO')))
    valor_metro_fio = models.FloatField()
    liga = models.ForeignKey(Liga, on_delete=PROTECT)
    quantidade_fio = models.IntegerField(default=0)
    comprimento_fio = models.FloatField(default=0)
    garantia = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    


    def __str__(self):
        return str(self.jogo_fio)



class Serrada(models.Model):
    serrada = models.IntegerField()
    data_inicial = models.DateTimeField()
    data_final = models.DateTimeField()
    maquina = models.ForeignKey(Maquina, on_delete=PROTECT)
    horimetro_inicial = models.IntegerField()
    horimetro_final = models.IntegerField()
    amperagem_max = models.DecimalField(max_digits=8, decimal_places=3)
    espessura_fio_inicial = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    espessura_fio_final = models.DecimalField(max_digits=6, decimal_places=3, default=0)    
    observacoes = models.TextField()
    periferica = models.DecimalField(max_digits=5, decimal_places=3)
    cala = models.IntegerField(default=10)
    jogo_fio = models.ForeignKey(Fio_diamantado, on_delete=PROTECT)
    consumo_kwh_fp = models.DecimalField(max_digits=7, decimal_places=3, default=0)
    consumo_kwh_p = models.DecimalField(max_digits=7, decimal_places=3, default=0)
    centro_de_custo = models.ForeignKey(Centro_de_Custo, on_delete=PROTECT,default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.serrada)



class BlocoSerrada(models.Model):
    serrada = ForeignKey(Serrada, on_delete=PROTECT)
    bloco = models.ForeignKey(Bloco, on_delete=models.PROTECT)
    comprimento = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    altura = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    largura = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.bloco)



class Parada(models.Model):
    serrada = models.ForeignKey(Serrada, on_delete=PROTECT)
    data_inicial = models.DateTimeField()
    data_final = models.DateTimeField() 
    motivo = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)




class Grupo(models.Model):
    grupo = models.CharField(max_length=50)

    def __str__(self):
        return str(self.grupo)

class Classe(models.Model):
    classe = models.CharField(max_length=50)

    def __str__(self):
        return str(self.classe)

class Produto(models.Model):
    produto = models.CharField(max_length=100)
    unidade = models.ForeignKey(Unidade, on_delete=PROTECT)
    grupo = models.ForeignKey(Grupo, on_delete=PROTECT)
    classe = models.ForeignKey(Classe, on_delete=PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
   # usuario = models.ForeignKey(User, on_delete=PROTECT)

    def  __str__(self):
        return str(self.produto)


class Chapas_produzidas(models.Model):
    serrada = models.ForeignKey(Serrada, on_delete=models.PROTECT)
    bloco = models.ForeignKey(Bloco, on_delete=models.PROTECT)
    comprimento = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    altura = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    largura = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    qtde_fios = models.IntegerField(default=0)
    quantidade = models.IntegerField()
    espessura = models.ForeignKey(Espessura, on_delete=models.PROTECT) 
    created = models.DateTimeField(auto_now_add=True)
  #  usuario = models.ForeignKey(User, on_delete=PROTECT)

    def __str__(self):
        return str(self.bloco)


class Aplicacao(models.Model):
    aplicacao = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return str(self.aplicacao)

class Despesa(models.Model):
    pedreira = models.ForeignKey(Pedreira, on_delete=PROTECT)
    centro_de_custo = models.ForeignKey(Centro_de_Custo, on_delete=PROTECT)
    aplicacao = models.ForeignKey(Aplicacao, on_delete=PROTECT)
    data = models.DateField()    
    valor = models.FloatField()
    descricao = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
  #  usuario = models.ForeignKey(User, on_delete=PROTECT)


    def __str__(self):
        return str(self.centro_de_custo)

class DespesaItem(models.Model):
    despesa = models.ForeignKey(Despesa, on_delete=PROTECT)
    produto = models.ForeignKey(Produto, on_delete=PROTECT)
    quantidade = models.FloatField()
    unidade = models.ForeignKey(Unidade, on_delete=PROTECT)
    preco = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
   # usuario = models.ForeignKey(User, on_delete=PROTECT)

    def __str__(self):
        return str(self.produto)

class Detalhe(models.Model):
    detalhe = models.CharField(max_length=50)

    def __str__(self):
        return str(self.detalhe)

class Qualidade(models.Model):
    qualidade = models.CharField(max_length=50)

    def __str__(self):
        return str(self.qualidade)
class Estoque_ladrilho(models.Model):
    material = models.ForeignKey(Material, on_delete=PROTECT)
    acabamento = models.ForeignKey(Acabamento, on_delete=PROTECT)
    qualidade = models.ForeignKey(Qualidade, on_delete=PROTECT)
    detalhe = models.ForeignKey(Detalhe, on_delete=PROTECT)
    quantidade = models.FloatField()
    comprimento = DecimalField(max_digits=6, decimal_places=3)
    espessura = DecimalField(max_digits=6, decimal_places=3)
    largura = DecimalField(max_digits=6, decimal_places=3)
    preco = models.FloatField()    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.material)

class Entrada_ladrilho(models.Model):
    material = models.ForeignKey(Material, on_delete=PROTECT)
    acabamento = models.ForeignKey(Acabamento, on_delete=PROTECT)
    qualidade = models.ForeignKey(Qualidade, on_delete=PROTECT)
    detalhe = models.ForeignKey(Detalhe, on_delete=PROTECT)
    quantidade = models.FloatField()
    comprimento = DecimalField(max_digits=6, decimal_places=3)
    espessura = DecimalField(max_digits=6, decimal_places=3)
    largura = DecimalField(max_digits=6, decimal_places=3)
    preco = models.FloatField()    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.material)

class Estoque_chapa(models.Model):
    bloco = models.ForeignKey(Bloco, on_delete=models.PROTECT)
    acabamento = models.ForeignKey(Acabamento, on_delete=PROTECT)
    qualidade = models.ForeignKey(Qualidade, on_delete=PROTECT)
    detalhe = models.ForeignKey(Detalhe, on_delete=PROTECT)
    quantidade = models.FloatField()
    comprimento = DecimalField(max_digits=6, decimal_places=3)
    espessura = DecimalField(max_digits=6, decimal_places=3)
    largura = DecimalField(max_digits=6, decimal_places=3)
    preco = models.FloatField()    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.material)

class Entrada_chapa(models.Model):
    bloco = models.ForeignKey(Bloco, on_delete=models.PROTECT)
    acabamento = models.ForeignKey(Acabamento, on_delete=PROTECT)
    qualidade = models.ForeignKey(Qualidade, on_delete=PROTECT)
    detalhe = models.ForeignKey(Detalhe, on_delete=PROTECT)
    quantidade = models.FloatField()
    comprimento = DecimalField(max_digits=6, decimal_places=3)
    espessura = DecimalField(max_digits=6, decimal_places=3)
    largura = DecimalField(max_digits=6, decimal_places=3)
    preco = models.FloatField()    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.material)

class BlocoItem(models.Model):
    bloco = models.ForeignKey(Bloco, on_delete=PROTECT)
    produto = models.ForeignKey(Produto, on_delete=PROTECT)
    unidade = models.ForeignKey(Unidade, on_delete=PROTECT)
    quantidade = models.FloatField()
    valor = models.FloatField()
    descricao = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)







class Empresa(models.Model):
    empresa = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    cep = models.CharField(max_length=6, default='60000')
    endereco = models.CharField(max_length=200)
    uf = CharField(max_length=2, default='CE')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.empresa)

class FioFatorConversao(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=PROTECT)
    fornecedor = models.ForeignKey(Pessoa, on_delete=PROTECT)
    dureza = models.IntegerField()
    fator = models.FloatField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.fator)

class LigaFatorConversao(models.Model):
    liga = models.ForeignKey(Liga, on_delete=PROTECT)
    dureza = models.IntegerField()
    fator = models.FloatField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



class Status_venda(models.Model):
    status_venda = CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.status_venda)

class Forma_pagamento(models.Model):
    forma_pagamento = models.CharField(max_length=100)    
    parcelas = models.IntegerField(default=1)
    intervalo = models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
  #  usuario = models.ForeignKey(User, on_delete=PROTECT)


    def __str__(self):
        return str(self.forma_pagamento)

class Frete(models.Model):
    frete = models.CharField(max_length=10)

    def __str__(self):
        return str(self.frete)

class Pedido_venda(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=PROTECT)
    pessoa = models.ForeignKey(Pessoa, on_delete=PROTECT, verbose_name="Cliente")
    data = models.DateField(default=timezone.now) 
    total = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    entrada = models.FloatField(default=100, verbose_name='Entrada %')
    forma_pagamento = models.ForeignKey(Forma_pagamento, on_delete=PROTECT)
    prazo_entrega = models.IntegerField(default=0)
    frete = models.ForeignKey(Frete, on_delete=PROTECT)
    status_venda = models.ForeignKey(Status_venda, on_delete=PROTECT, verbose_name="Status")
    observacao = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    #created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
   # usuario = models.ForeignKey(User, on_delete=PROTECT)

    def __str__(self):
        return str(f'{self.pessoa} {self.total} {self.data}')

    #def save(self, *args, **kwargs):
    #    pdtotal = Pedido_venda_item.objects.all().values()
    #    self.total = pdtotal['quantidade'] * pdtotal['preco'] * pdtotal['comprimento'] * pdtotal['largura']
    #    if pdtotal['percentual_ipi'] > 0:
    #        pdtotal['valor'] += pdtotal['valor']*(pdtotal['percentual_ipi']/100)
    #    self.save()
    #    super(Pedido_venda, self).save(*args, **kwargs)

class Pedido_venda_item(models.Model):
    pedido_venda = models.ForeignKey(Pedido_venda, on_delete=PROTECT)
    grupo = models.ForeignKey(Grupo, on_delete=PROTECT)
    material = models.ForeignKey(Material, on_delete=PROTECT)
    un = models.ForeignKey(Un,on_delete=PROTECT, default='M2')
    quantidade = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    preco = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    altura_espessura = models.DecimalField(max_digits=10, decimal_places=3, default=0, verbose_name="Alt/Esp")
    comprimento =  models.DecimalField(max_digits=10, decimal_places=3, default=0)
    largura =  models.DecimalField(max_digits=10, decimal_places=3, default=0)    
    acabamento = models.ForeignKey(Acabamento, on_delete=PROTECT)
    bloco = models.ForeignKey(Bloco, on_delete=PROTECT, blank=True, null=True)
    #identificacao = models.CharField(max_length=20, null=True)
    percentual_ipi = models.DecimalField(max_digits=6, decimal_places=3, default=5) 
    valor = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)
   # usuario = models.ForeignKey(User, on_delete=PROTECT)

    def __str__(self):
        return "ID:"+str(self.id)
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens do Pedido'
    def save(self, *args, **kwargs): 
           
        if str(self.un) == 'M2':
            self.valor = self.quantidade * self.preco * self.comprimento * self.largura
        elif str(self.un) == 'M3':            
            self.valor = self.quantidade * self.preco * self.altura_espessura * self.comprimento * self.largura
        else:
            self.valor = self.quantidade * self.preco        
        if self.percentual_ipi>0:
            self.valor += self.valor*(self.percentual_ipi/100)        
        self.pedido_venda.total += self.valor
        self.pedido_venda.save()
        super(Pedido_venda_item, self).save(*args, **kwargs)

"""
class Mes(models.Model):
    mes = models.PositiveSmallIntegerField(primary_key=True)

    def __str__(self):
        return str(self.mes)

"""
class Linha_Resinamento(models.Model):
    linha = CharField(max_length=15)

    def __str__(self):
        return str(self.linha)

class Setor(models.Model):
    setor = models.CharField(max_length=100)

    def __str__(self):
        return str(self.setor)

class Operador(models.Model):
    operador = models.CharField(max_length=100)
    setor = models.ForeignKey(Setor, on_delete=PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    #usuario = models.ForeignKey(User, on_delete=PROTECT)
    def __str__(self):
        return str(self.operador)

class Resina(models.Model):
    resina = models.CharField(max_length=100)
    dados_tecnicos = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
  #  usuario = models.ForeignKey(User, on_delete=PROTECT)

    def __str__(self):
        return str(self.resina)
class Resina_Valor(models.Model):
    resina = models.ForeignKey(Resina, on_delete=PROTECT)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    un = models.ForeignKey(Un, on_delete=PROTECT)
    ativo = models.BooleanField(default=True)
    data_compra = models.DateField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
  #  usuario = models.ForeignKey(User, on_delete=PROTECT)

    def __str__(self):
        return str(self.resina)
class Resinamento(models.Model):
    linha = models.ForeignKey(Linha_Resinamento, on_delete=PROTECT)
    data = models.DateField(default=timezone.now())
    operador = models.ForeignKey(Operador, on_delete=PROTECT)
    bloco = models.ForeignKey(Bloco, on_delete=PROTECT, default=2)
    quantidade_de_chapas = models.PositiveIntegerField(default=0)
    observacao = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.data)
"""     
class Resinamento_Bloco(models.Model):
    resinamento_id = models.ForeignKey(Resinamento, on_delete=PROTECT)
    bloco = models.ForeignKey(Bloco, on_delete=PROTECT)
    quantidade_de_chapas = models.PositiveIntegerField()
    observacao = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
"""

class Resinamento_Insumo(models.Model):
    #resinamento_bloco_id = models.ForeignKey(Resinamento_Bloco, on_delete=PROTECT)
    resina = models.ForeignKey(Resina, on_delete=PROTECT)
    unidade = models.ForeignKey(Unidade_de_Medida, on_delete=PROTECT)
    quantidade = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)




class Resinamento_item(models.Model):
    resinamento_id = ForeignKey(Resinamento, on_delete=PROTECT, verbose_name="Insumo")
    #bloco = models.ForeignKey(Bloco, on_delete=PROTECT)
    resina = models.ForeignKey(Resina, on_delete=PROTECT)
    #quantidade_de_chapas = models.FloatField()
    quantidade_insumo = models.FloatField(default=0)
    unidade = models.ForeignKey(Unidade, on_delete=PROTECT, default=1)
    frequencia = models.PositiveIntegerField(default=1) 
    #observacao = models.CharField(max_length=200, blank=True)
 #   usuario = models.ForeignKey(User, on_delete=PROTECT)

class Parada_Resinamento(models.Model):
    resinamento_id = models.ForeignKey(Resinamento, on_delete=PROTECT)
    data_inicial = models.DateTimeField(default=timezone.now)
    data_final = models.DateTimeField() 
    motivo = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
class Faturamento(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=PROTECT)
    ano = models.IntegerField()
    mes = models.IntegerField(choices=MES_CHOICES)
    valor_interno = models.FloatField(default=0)
    valor_externo = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.ano} {self.mes} {self.empresa} {self.valor_interno} {self.valor_externo}'
    """
    usuario = models.ForeignKey(User, on_delete=PROTECT)
    
    def form_valid(self, form):
        form.instance.usuario = self.resquest.user
        url = super().form_valid(form)
        return url

"""
class Faturamento_view(models.Model):
    id = models.IntegerField(primary_key=True)
    empresa = models.CharField(max_length=100)
    ano = models.IntegerField()
    mes = models.IntegerField()
    mes_desc = models.CharField(max_length=100)
    valor_interno = models.FloatField(default=0)
    valor_externo = models.FloatField(default=0)
    total = models.FloatField(default=0)

    class Meta:
        managed=False
        db_table='faturamento_view'        
"""
VIEW_SQL = 
    SELECT * FROM public.vw_serrada
"""

"""
class Vw_serrada(pg.View):
    serrada = models.IntegerField(primary_key=True)
    bloco = models.CharField(max_length=15)
    maquina = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    comprimento = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    altura = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    largura = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    qtde_fios = models.IntegerField()
    jogo_fio = models.IntegerField()    
    m3_liq = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    comprimento_bru = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    altura_bru =models.DecimalField(max_digits=6, decimal_places=3, default=0)
    largura_br = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    m3_bru = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    m3_perda = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    prd_fio_m2  = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    m2  = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    dureza = models.IntegerField(default= True)
    fator = models.FloatField(default=1)
    jogo_fio = models.IntegerField()
    qtde_fios = models.IntegerField()
    qtde_chapas  = models.IntegerField()
    garantia_fio  = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    custo_fio_por_m2  = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    garantia_fio  = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    custo_bloco = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    folha = models.FloatField()
    mes = models.IntegerField(default=0)
    ano = models.IntegerField(default=0)
    custo_m2 = models.FloatField()

    class Meta:
      managed = False

"""
class Folha_de_Pagamento(models.Model):
    centro_de_custo = models.ForeignKey(Centro_de_Custo, on_delete=Node, default=1)
    ano = models.IntegerField(default=timezone.now().year)
    mes = models.IntegerField(choices=MES_CHOICES, default=1)
    qtde_funcionarios = models.IntegerField()
    folha = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.centro_de_custo)


"""
VIEW_SQL = 
    SELECT * FROM public.view_serrada
"""

class View_serrada(models.Model):
    serrada = models.IntegerField(primary_key=True)
    bloco = models.CharField(max_length=15, default=0)
    material = models.CharField(max_length=100, default='')
    comprimento = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    altura = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    largura = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    m3_bruto = models.DecimalField(max_digits=15, decimal_places=3, default=0) 
    m3_chapas_produzidas = models.DecimalField(max_digits=15, decimal_places=3, default=0)   
    m3_liquido = models.DecimalField(max_digits=15, decimal_places=3, default=0)    
    m3_perda = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    m3_perda_real = models.DecimalField(max_digits=15, decimal_places=3, default=0)   
    m3_perda_com_borda_chapa = models.DecimalField(max_digits=15, decimal_places=3, default=0)   
    m2  = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    valor_do_bloco = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    valor_m3 = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    custo_m2_sem_borda = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    custo_m2_com_borda = models.DecimalField(max_digits=15, decimal_places=3, default=0)

    jogo_fio_id = models.IntegerField()
    quantidade_fio = models.IntegerField()
    custo_fio_por_m2 = models.DecimalField(max_digits=15, decimal_places=2, default=0)  
    custo_fio_por_m2_aplicado = models.DecimalField(max_digits=15, decimal_places=2, default=0)  
    qtde_chapas  = models.IntegerField(default=0)
    espessura = models.DecimalField(max_digits=6, decimal_places=3, default=0) 
    data_inicial = models.DateTimeField()
    data_final = models.DateTimeField()
    maquina = models.CharField(max_length= 100)
    horimetro_inicial = models.IntegerField()
    horimetro_final = models.IntegerField()
    amperagem_max = models.DecimalField(max_digits=8, decimal_places=3, default=0)
    espessura_fio_inicial = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    espessura_fio_final = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    qtde_fios_aplicado = models.IntegerField()
    prd_fio_m2 = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    observacoes = models.TextField()
    periferica = models.DecimalField(max_digits=5, decimal_places=3)
    cala = models.IntegerField(default=10)
    consumo_kwh_p = models.DecimalField(max_digits=7, decimal_places=3, default=0)
    consumo_kwh_fp = models.DecimalField(max_digits=7, decimal_places=3, default=0)
    
    mes = models.IntegerField(default=0)
    ano = models.IntegerField(default=0)    
    class Meta:
        managed=False
        db_table='view_serrada'

class View_producao_fio(models.Model):
    maquina = models.CharField(max_length= 100)
    jogo_fio_id = models.IntegerField(primary_key=True)
    liga = models.CharField(max_length= 25)
    valor_metro_fio =  models.FloatField(default=0)
    m3_bruto = models.DecimalField(max_digits=15, decimal_places=3, default=0)    
    m3_liquido = models.DecimalField(max_digits=15, decimal_places=3, default=0) 
    m2  = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    espessura_fio = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    prd_fio_m2 = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    dureza = models.IntegerField(default=0)
    class Meta:
        managed=False
        db_table='view_producao_fio'

class View_producao_fio_resumo(models.Model):
    maquina = models.CharField(max_length= 100)
    jogo_fio_id = models.IntegerField(primary_key=True)
    liga = models.CharField(max_length= 25)
    valor_metro_fio =  models.FloatField(default=0)
    m3_bruto = models.DecimalField(max_digits=15, decimal_places=3, default=0)    
    m3_liquido = models.DecimalField(max_digits=15, decimal_places=3, default=0) 
    m2  = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    garantia_do_fio = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    saldo = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    espessura_fio = models.DecimalField(max_digits=6, decimal_places=3, default=0)
    prd_fio_m2 = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    prd_fio_m2_dureza = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    class Meta:
        managed=False
        db_table='view_producao_fio_resumo'

class Custos_Pedreira(models.Model):
    id = models.AutoField(primary_key=True)    
    ano = models.IntegerField(default=timezone.now().year)
    mes = models.IntegerField(choices=MES_CHOICES)
    pedreira = models.ForeignKey(Pedreira, on_delete=models.PROTECT) 
    valor = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 
    usuario = models.ForeignKey(User, default=8, on_delete=PROTECT)

    def __str__(self):
        return str(self.pedreira)   


class Producao_Pedreira(models.Model):
    custos_pedreira = models.ForeignKey(Custos_Pedreira, on_delete=PROTECT)
    material = models.ForeignKey(Material, on_delete=PROTECT)
    m3 = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 
    usuario = models.ForeignKey(User, default=8, on_delete=PROTECT)






                

