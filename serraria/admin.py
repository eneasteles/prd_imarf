from django.contrib import admin
from django.contrib.admin.filters import ListFilter

from producao.models import *

admin.site.site_header = 'SISTEMA DE CONTROLE DE PRODUÇÃO - IMARF'
admin.site.site_title = 'PRODUÇÃO'
admin.site.index_title = 'PCP IMARF'

#Acabamento, Bloco, Chapa, Fio_diamantado, Insumo, Maquina, Material, Observacao_chapa, Pessoas, Serrada, Status_bloco, Status_chapa, Chapas_produzidas, Espessura, Unidade
#class Chapas_produzidasinline(admin.TabularInline):
#    model = Chapas_produzidas
#    extra = 1






