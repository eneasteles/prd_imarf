from django.urls import path

from .views import * 

urlpatterns = [
    #path('current_datetime/', views.current_datetime, name='current_datetime'),
    # path('', views.home, name='home')
    #path('', views.PaginaInicial.as_view(), name='index'),
    #path('teste', views.IndexView.as_view(), name='inicio'),
    path('', SobreView.as_view(), name='sobre'),
    path('pd_faturamento/', pd_faturamento, name='pd_faturamento'),
    
]