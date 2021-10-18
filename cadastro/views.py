from django.db.models import Sum, Max, Min, Avg
from django.db.models.aggregates import Avg, Min
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from producao.models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

# Create your views here.

class BlocoCreate(CreateView):
    model = Bloco
    fields = ['bloco']
    template_name = 'cadastro/form.html'
    success_url = reverse_lazy('')

class MaterialCreate(CreateView):
    model = Material
    fields = ['material','dureza']
    template_name = 'cadastro/form_material.html'
    success_url = reverse_lazy('')

class FaturamentoCreate(CreateView):
    model = Faturamento
    fields = ['empresa','ano', 'mes', 'valor_interno', 'valor_externo']
    template_name = 'cadastro/form_faturamento.html'
    success_url = reverse_lazy('lista-faturamento')
###########  update  ################

class MaterialUpdate(UpdateView):
    model = Material
    fields = ['material','dureza']
    template_name = 'cadastro/form_material.html'
    success_url = reverse_lazy('')

class FaturamentoUpdate(UpdateView):
    model = Faturamento
    fields = ['empresa','ano', 'mes', 'valor_interno', 'valor_externo']
    template_name = 'cadastro/form_faturamento.html'
    success_url = reverse_lazy('lista-faturamento')
"""
    def get_object(self, queryset= None):
        self.object = get_object_or_404(Faturamento, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object
"""
###########  delete  ################

class FaturamentoDelete(DeleteView):
    model = Faturamento
    template_name = 'cadastro/form-deletar-faturamento.html'
    success_url = reverse_lazy('lista-faturamento')
"""
    def get_object(self, queryset= None):
        self.object = get_object_or_404(Faturamento, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object
"""


###########  list  ################

class FaturamentoList(LoginRequiredMixin ,ListView):
    login_url = reverse_lazy('login')
    model = Faturamento
    template_name = 'cadastro/lista/lista-faturamento.html'
"""
    def get_queryset(self):
        self.object_list = Faturamento.objects.filter(usuario=self.request.user)
        return self.object_list
"""
class SerradaList(LoginRequiredMixin ,ListView):
    login_url = reverse_lazy('login')
    model = Serrada
    template_name = 'cadastro/lista/lista-serrada.html'
"""
    def get_queryset(self):
        self.object_list = Faturamento.objects.filter(usuario=self.request.user)
        return self.object_list
"""
class SerradaList2(LoginRequiredMixin ,ListView):
    login_url = reverse_lazy('login')
    model = View_serrada
    template_name = 'cadastro/lista/lista-serrada2.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SerradaList2, self).get_context_data(*args, **kwargs)
        context['m3_liquido'] = View_serrada.objects.aggregate(Sum('m3_liquido'))
        context['m2'] = View_serrada.objects.aggregate(Sum('m2'))
        context['qtde_chapas'] = View_serrada.objects.aggregate(Sum('qtde_chapas'))
        context['m3_perda_com_borda_chapa'] = View_serrada.objects.aggregate(Sum('m3_perda_com_borda_chapa'))
        return context

class ProducaoFio(LoginRequiredMixin ,ListView):
    login_url = reverse_lazy('login')
    model = View_producao_fio
    template_name = 'cadastro/lista/lista-fio-producao.html'

class ProducaoFioResumo(LoginRequiredMixin ,ListView):
    login_url = reverse_lazy('login')
    model = View_producao_fio_resumo
    template_name = 'cadastro/lista/lista-fio-producao-resumo.html'