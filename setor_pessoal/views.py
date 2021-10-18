from django.db.models import Sum, Max, Min, Avg
from django.db.models.aggregates import Avg, Min
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

# Create your views here.
class Resumo(LoginRequiredMixin ,ListView):
    login_url = reverse_lazy('login')
    model = Resumo_Funcionarios_View
    template_name = 'setor_pessoal/resumo.html'

    
