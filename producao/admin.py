from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.admin.filters import ListFilter

from . models import *

admin.site.site_header = 'SISTEMA DE CONTROLE DE PRODUÇÃO - IMARF'
admin.site.site_title = 'PRODUÇÃO'
admin.site.index_title = 'PCP IMARF'

#Acabamento, Bloco, Chapa, Fio_diamantado, Insumo, Maquina, Material, Observacao_chapa, Pessoas, Serrada, Status_bloco, Status_chapa, Chapas_produzidas, Espessura, Unidade
class Chapas_produzidasinline(admin.TabularInline):
    model = Chapas_produzidas
    extra = 1

class BlocoIteminline(admin.TabularInline):    
    model = BlocoItem
    extra = 1


@admin.register(Bloco)
class BlocoAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usuario_id=request.user)
    
    ordering = ('bloco',)
    list_filter = ('status','tipo','material',)
    list_display = ('bloco','material','tipo','comprimento','altura','largura','status')
    #list_editable = ('comprimento','altura','largura','status')
    
    search_fields = ('bloco',)
    inlines = [
        BlocoIteminline
    ]

class ProducaoPedreiraInline(admin.TabularInline):
    model = Producao_Pedreira
    extra = 1
@admin.register(Custos_Pedreira)
class CustoPedreiraAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usuario_id=request.user)
    
    list_display = ('pedreira','ano','mes', 'valor')
    inlines = [
        ProducaoPedreiraInline
    ]

class Resina_ValorInline(admin.TabularInline):
    model = Resina_Valor
    extra = 1

@admin.register(Resina)
class ResinaAdmin(admin.ModelAdmin):
    list_display = ('resina','dados_tecnicos')
    inlines = [
        Resina_ValorInline
    ]
class Resinamento_itemInline(admin.TabularInline):    
    model = Resinamento_item
    extra = 1
class Resinamento_Insumo_Inline(admin.TabularInline):
    model = Resinamento_Insumo
    extra = 1
"""class Resinamento_Bloco_Inline(admin.TabularInline):
    model = Resinamento_Bloco
    extra = 1
    inlines = [
        Resinamento_Insumo_Inline,
    ]
"""

class ParadaResinamentoinline(admin.TabularInline):
    model = Parada_Resinamento
    extra = 1
class ResinamentoAdmin(admin.ModelAdmin):
    list_display = ('data','bloco','quantidade_de_chapas','id')
    inlines = [
        #Resinamento_Bloco_Inline,
        Resinamento_itemInline,
        ParadaResinamentoinline,
        
    ]
class Fio_diamantadoinline(admin.TabularInline):
    model = Fio_diamantado
    extra = 1
class FioAdmin(admin.ModelAdmin):
    inlines = [
        Fio_diamantadoinline
    ]

class DespesaIteminline(admin.TabularInline):
    model = DespesaItem
    extra = 1
class DespesaItemAdmin(admin.ModelAdmin):
    inlines = [
        DespesaIteminline
    ]


class Paradainline(admin.TabularInline):
    model = Parada
    extra = 1

class LigaFatorConversaoinline(admin.TabularInline):
    model = LigaFatorConversao
    extra = 1
@admin.register(Liga)    
class LigaAdmin(admin.ModelAdmin):
    inlines = [
        LigaFatorConversaoinline
    ]
    
        
class Forma_pagamento_inline(admin.TabularInline):
    model = Forma_pagamento
    extra = 1

class Pedido_venda_item_inline(admin.TabularInline):
    model = Pedido_venda_item
    extra = 1

@admin.register(Pedido_venda)    
class Pedido_venda_Admin(admin.ModelAdmin):    
    list_display = ('id','pessoa','data')
    list_display_links = ('id','pessoa','data')
    list_filter = ('id','pessoa')
    list_per_page = 10
    search_fields = ['id']
    inlines = [
        Pedido_venda_item_inline,
       # Forma_pagamento_inline,
    ]
@admin.register(Serrada)
class SerradaAdmin(admin.ModelAdmin):
    list_display = ('serrada','data_final', 'created')
    inlines = [
        #BlocoSerradaInline,
        Chapas_produzidasinline,
        Paradainline,
        
    ]
@admin.register(Faturamento)
class FaturamentoAdmin(admin.ModelAdmin):
    list_display = ('ano','mes', 'empresa', 'valor_interno','valor_externo')
    ordering =('ano','mes', 'empresa',)
   

admin.site.register(Material)
#admin.site.register(Bloco, BlocoAdmin)
admin.site.register(Status_bloco)
admin.site.register(Chapa)
admin.site.register(Status_chapa)
admin.site.register(Espessura)
admin.site.register(Acabamento)
admin.site.register(Observacao_chapa)
admin.site.register(Insumo)
admin.site.register(Unidade)
admin.site.register(Un)
admin.site.register(Maquina)     #       admin.site.register()
#admin.site.register(Serrada, SerradaAdmin) #, ChapasAdmin
admin.site.register(Fio_diamantado)
admin.site.register(Pessoa)
admin.site.register(Grupo)
admin.site.register(Produto)
admin.site.register(Classe)
admin.site.register(Centro_de_Custo)
admin.site.register(Despesa, DespesaItemAdmin)
admin.site.register(Pedreira)
admin.site.register(Aplicacao)
admin.site.register(Detalhe)
admin.site.register(Qualidade)
admin.site.register(Entrada_chapa)
admin.site.register(Entrada_ladrilho)
#admin.site.register(Liga, LigaAdmin)
admin.site.register(Forma_pagamento)
#admin.site.register(Pedido_venda, Pedido_venda_Admin)
admin.site.register(Empresa)
admin.site.register(Status_venda)
admin.site.register(Frete)
admin.site.register(FioFatorConversao)
admin.site.register(Resinamento, ResinamentoAdmin)
admin.site.register(Operador)
admin.site.register(Setor)
admin.site.register(Folha_de_Pagamento)
#admin.site.register(Faturamento,FaturamentoAdmin)

#admin.site.register(Custos_Pedreira, CustoPedreiraAdmin)
admin.site.register(Linha_Resinamento)


