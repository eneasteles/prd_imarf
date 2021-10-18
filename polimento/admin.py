from producao.models import Qualidade
from polimento.models import Abrasivo, Chapas_Polidas, Jogo_de_Abrasivos, Parada_Politriz, Polimento, Qualidade_Polimento, Tipo_Polimento
from django.contrib import admin
from django.contrib.admin.sites import site

# Register your models here.
class ChapasPolidasInline(admin.TabularInline):    
    model = Chapas_Polidas
    extra = 1
class ParadaPolitrizInline(admin.TabularInline):
    model = Parada_Politriz
    extra = 1
class Jogo_de_AbrasivoInline(admin.TabularInline):
    model = Jogo_de_Abrasivos
    extra = 1
@admin.register(Polimento)
class PolimentoAdmin(admin.ModelAdmin):
    ordering = ('data',)
    list_display = ('data','maquina','turno')
    inlines = [
        ChapasPolidasInline,
        ParadaPolitrizInline,
        Jogo_de_AbrasivoInline,
    ]


admin.site.register(Abrasivo)
admin.site.register(Qualidade_Polimento)
admin.site.register(Tipo_Polimento)

