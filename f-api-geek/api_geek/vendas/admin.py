from django.contrib import admin
from vendas.models import Categoria, Franquia, Produto, Venda

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)  
    ordering = ('nome',)  

@admin.register(Franquia)
class FranquiaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)  
    ordering = ('nome',)  

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'quantidade', 'categoria', 'franquia')
    search_fields = ('nome',)  
    list_filter = ('categoria', 'franquia')  
    ordering = ('nome',)  
    list_editable = ('quantidade', 'preco')  

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'produto', 'quantidade', 'valor_total', 'data_hora')
    readonly_fields = ('valor_total',)
    search_fields = ('cliente',)  
    list_filter = ('produto', 'data_hora')  
    ordering = ('-data_hora',)  
