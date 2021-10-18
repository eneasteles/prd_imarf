from django.contrib import admin
from custos_gerais.models import Custo_Geral, Energia, Item_de_Producao, Custo_Geral_Item

class Custo_Geral_ItemInline(admin.TabularInline):
    model = Custo_Geral_Item
    extra = 1

class Custo_GeralAdmin(admin.ModelAdmin):
    list_display = ('ano', 'mes', 'producao_m2')
    inlines = [
        Custo_Geral_ItemInline
        ]
@admin.register(Energia)
class Energia_Admin(admin.ModelAdmin):
    list_display = ('ano','mes','consumo_hp','consumo_hfp','valor')


admin.site.register(Item_de_Producao)
#admin.site.register(Custo_Geral_Item)
admin.site.register(Custo_Geral, Custo_GeralAdmin)
#admin.site.register(Custos_Gerais_Itens)
