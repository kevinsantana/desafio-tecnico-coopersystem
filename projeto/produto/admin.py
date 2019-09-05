from django.contrib import admin
from .models import Produto


class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'disponivel',        
        'preco',
        'quantidade',        
    )
    search_fields = ('produto',)
    list_filter = ('disponivel',)
