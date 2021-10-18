from django.urls import path

from .views import *

urlpatterns = [
    path('setor_pessoal/resumo/', Resumo.as_view(), name='resumo'),
]