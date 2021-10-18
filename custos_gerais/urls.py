from django.urls import path

from .views import *

urlpatterns = [
    path('custos_gerais/sum/', example, name='sum_m3_liquido'),
    path('custos_gerais/', main_view, name='pandas-serraria'),
    path('custos_gerais/serrada/', pd_serrada, name='pd_serrada'),
    path('custos_gerais/serrada/total/', pd_serrada_total, name='pd_serrada_total'),
    path('custos_gerais/serrada/soma/', pd_serrada_soma, name='pd_serrada_soma'),
    path('custos_gerais/serrada/media/', pd_serrada_media, name='pd_serrada_media'),
    path('custos_gerais/pd_faturamento', pd_faturamento, name='pd_faturamento'),
]