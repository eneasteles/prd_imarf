from estoque.models import Estoque, Tipo_Produto
from django.contrib import admin

# Register your models here.

@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('material', 'tipo',  'acabamento','qualidade','detalhe','unidade', 'quantidade', 'comprimento', 'altura_espessura','largura','preco')
    list_filter = ( 'material', 'tipo')

admin.site.register(Tipo_Produto)

