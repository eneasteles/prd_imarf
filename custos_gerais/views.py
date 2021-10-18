from django.db.models import Sum, Max, Min, Avg
from django.db.models.aggregates import Avg, Min
from django.shortcuts import render
from producao.models import Faturamento_view, View_serrada, Faturamento
import pandas as pd
import numpy as np
import re
#import matplotlib.pyplot as plt

def example(request):
    _sum = View_serrada.objects.all().aggregate(sum=Sum('m3_liquido'))
    _max = View_serrada.objects.all().aggregate(max=Max('m3_liquido'))
    _min = View_serrada.objects.all().aggregate(min=Min('m3_liquido'))
    _avg = View_serrada.objects.all().aggregate(avg=Avg('m3_liquido'))
    return render(request, 'custos_gerais/view_serrada_sum.html', {'sum':_sum, 'max':_max, 'min':_min, 'avg':_avg})

def main_view(request):
    qs = View_serrada.objects.all().values()
    data = pd.DataFrame(qs)
   # data.loc['m3_bruto'] = data.sum()

    context = {
        'df': data.to_html(),
        'describe': data.describe().to_html()
    }

    return render(request, 'custos_gerais/view_serraria.html', context)

def pd_serrada(request):
    qs = View_serrada.objects.all().values()
    data = pd.DataFrame(qs)
    #data = data_.replace('[^\d.]', '', regex=True).astype(float)
    producao_por_material = data[["mes","ano","material","espessura","qtde_chapas","m2","m3_liquido","m3_perda_com_borda_chapa"]].groupby(["mes","ano","material","espessura"]).sum(numeric_only=False)
    

    context = {

        'df': producao_por_material.to_html(classes=['table', 'table-striped', 'table-hover']),
    
        'describe': producao_por_material.describe().to_html(classes=['table', 'table-striped', 'table-hover']),
        
    }
    return render(request, 'custos_gerais/serrada.html', context)

   
def pd_serrada_soma(request):
    pd.set_option('display.precision', 2)

    qs = View_serrada.objects.all().values()
    data_soma = pd.DataFrame(qs)  
    #data_soma = data_soma.replace('[^\d.]', '', regex=True).astype(float)
    
    data_soma = data_soma.drop(columns=['material','espessura','maquina','qtde_fios_aplicado','prd_fio_m2','consumo_kwh','quantidade_fio','custo_fio_por_m2','custo_fio_por_m2_aplicado','valor_do_bloco','valor_m3','custo_m2_sem_borda','custo_m2_com_borda','bloco','comprimento','altura','largura','serrada','data_inicial','data_final','observacoes','periferica','cala','jogo_fio_id','horimetro_inicial','horimetro_final','amperagem_max','espessura_fio_inicial','espessura_fio_final'])
    
    #data_soma.loc['Total'] = data_soma.sum()
    data_soma.loc['Total'] = data_soma.sum()
    #data_soma2 = data_soma.groupby(['ano','mes']).sum()
    context = {
        'df': data_soma.to_html(classes=['table', 'table-striped', 'table-hover']),
        'describe': data_soma.describe().to_html(),        
    }
    return render(request, 'custos_gerais/serrada_soma.html', context)


def pd_serrada_total(request):
    qs = View_serrada.objects.all().values()
    pd.options.display.float_format = '{:,.2f}'.format
    pd.options.display.colheader_justify = 'center'

    data = pd.DataFrame(qs)
    producao_total = data[["mes","ano","qtde_chapas","m2","m3_liquido","m3_perda_com_borda_chapa"]].groupby(["mes","ano"]).sum(numeric_only=False)

    
    context = {       
        'df': producao_total.to_html(classes=['table', 'table-striped', 'table-hover']),
        #'describe': data.describe().to_html(classes=['table', 'table-striped', 'table-hover']),                 
    }
    return render(request, 'custos_gerais/serrada_total.html', context)

def pd_serrada_media(request):
    qs = View_serrada.objects.all().values()
    pd.options.display.float_format = '{:,.2f}'.format
    pd.options.display.colheader_justify = 'center'
    data = pd.DataFrame(qs)
    media_por_material = data[["mes","ano","material","m2"]].groupby(["mes","ano","material"]).median(numeric_only=False)
    producao_total = data[["mes","ano","qtde_chapas","m2","m3_liquido","m3_perda_com_borda_chapa"]].groupby(["mes","ano"]).sum(numeric_only=False)
    producao_total_anual = data[["ano","qtde_chapas","m2","m3_liquido","m3_perda_com_borda_chapa"]].groupby(["ano"]).sum(numeric_only=False)

    context = {

        'df':     media_por_material.to_html(classes=['table', 'table-striped', 'table-hover']),
        'describe': media_por_material.describe().to_html(classes=['table', 'table-striped', 'table-hover']), 
        'total': producao_total.to_html(classes=['table', 'table-striped', 'table-hover']),
        'anual': producao_total_anual.to_html(classes=['table', 'table-striped', 'table-hover']),
        
    }
    return render(request, 'custos_gerais/serrada_media.html', context)

def pd_faturamento(request):
    qs = Faturamento_view.objects.all().values()
    pd.options.display.float_format = '{:,.2f}'.format
    pd.options.display.colheader_justify = 'left'
    
    
    data = pd.DataFrame(qs)
    #media_por_material = data[["mes","ano","material","m2"]].groupby(["mes","ano","material"]).median(numeric_only=False)
    faturamento_mensal = data[["mes","mes_desc","ano","valor_interno","valor_externo","total"]].groupby(["ano","mes","mes_desc"]).sum(numeric_only=False)
    faturamento_total_anual = data[["ano","valor_interno","valor_externo","total"]].groupby(["ano"]).sum(numeric_only=False)
    faturamento_empresa_anual = data[["empresa","ano","valor_interno","valor_externo","total"]].groupby(["empresa","ano"]).sum(numeric_only=False)

    context = {

        #'df':     media_por_material.to_html(classes=['table', 'table-striped', 'table-hover']),
        #'faturamento_empresa_anual': media_por_material.describe().to_html(classes=['table', 'table-striped', 'table-hover']), 
        'faturamento_mensal': faturamento_mensal.to_html(classes=['table', 'table-striped', 'table-hover']),
        'anual': faturamento_total_anual.to_html(classes=['table', 'table-striped', 'table-hover']),
        'faturamento_empresa_anual': faturamento_empresa_anual.to_html(classes=['table', 'table-striped', 'table-hover']),
        
    }
    return render(request, 'custos_gerais/faturamento.html', context)