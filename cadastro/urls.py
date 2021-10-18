from django.urls import path

from .views import *

urlpatterns = [
    path('cadastrar/bloco', BlocoCreate.as_view(), name="cadastrar-bloco"),
    path('cadastrar/material', MaterialCreate.as_view(), name="cadastrar-material"),
    path('cadastrar/faturamento', FaturamentoCreate.as_view(), name="cadastrar-faturamento"),

    path('editar/material/<int:pk>', MaterialUpdate.as_view(), name='editar-material'),
    path('editar/faturamento/<int:pk>', FaturamentoUpdate.as_view(), name='editar-faturamento'),

    path('deletar/faturamento/<int:pk>', FaturamentoDelete.as_view(), name='deletar-faturamento'),
    path('listar/faturamento/', FaturamentoList.as_view(), name='lista-faturamento'),
    path('listar/serrada/', SerradaList.as_view(), name='lista-serrada'),
    path('listar/serrada2/', SerradaList2.as_view(), name='lista-serrada2'),
    path('listar/fio/', ProducaoFio.as_view(), name='lista-fio-producao'),
    path('listar/fio/resumo/', ProducaoFioResumo.as_view(), name='lista-fio-producao-resumo'),
]