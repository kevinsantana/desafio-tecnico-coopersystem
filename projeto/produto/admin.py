from django.contrib import admin
from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'disponivel',        
        'preco',
        'estoque',        
    )
    search_fields = ('produto',)
    list_filter = ('disponivel',)
