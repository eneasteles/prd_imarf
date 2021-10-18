from producao.models import Faturamento
from django.shortcuts import render
from django.views.generic import TemplateView

from django.db.models import Sum, Max, Min, Avg
from django.db.models.aggregates import Avg, Min
import pandas as pd



# Create your views here.
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def home(request):
    return HttpResponse('Página Inicial')

class IndexView(TemplateView):
    template_name = 'index.html'


class PaginaInicial(TemplateView):
    template_name = 'producao/modelo.html'

class SobreView(TemplateView):
    template_name = 'producao/sobre.html'

def pd_faturamento(request):
    qs = Faturamento.objects.all().values()
    pd.options.display.float_format = '{:,.2f}'.format
    pd.options.display.colheader_justify = 'center'
    data = pd.DataFrame(qs)
    #media_por_material = data[["mes","ano","material","m2"]].groupby(["mes","ano","material"]).median(numeric_only=False)
    #producao_total = data[["mes","ano","qtde_chapas","m2","m3_liquido","m3_perda_com_borda_chapa"]].groupby(["mes","ano"]).sum(numeric_only=False)
    producao_total_anual = data[["ano","mes","empresa","valor_interno","valor_externo"]].groupby(["ano"]).sum(numeric_only=False)

    context = {

        #'df':     media_por_material.to_html(classes=['table', 'table-striped', 'table-hover']),
        #'describe': media_por_material.describe().to_html(classes=['table', 'table-striped', 'table-hover']), 
        #'total': producao_total.to_html(classes=['table', 'table-striped', 'table-hover']),
        'anual': producao_total_anual.to_html(classes=['table', 'table-striped', 'table-hover']),
        
    }
    return render(request, 'producao/faturamento.html', context)