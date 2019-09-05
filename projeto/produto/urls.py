from django.urls import path
from projeto.produto import views as v

app_name = 'produto'

urlpatterns = [
    path('', v.ProdutoList.as_view(), name='produto_list'), # apresenta todos os produtos
    path('<int:pk>/', v.produto_detail, name='produto_detail'), # exibe o produto a partir da sua PK
    path('add/', v.ProdutoCreate.as_view(), name='produto_add'), # cria um novo produto
    path('<int:pk>/edit/', v.ProdutoUpdate.as_view(), name='produto_edit'), # edita um produto
    path('<int:pk>/json/', v.produto_json, name='produto_json'), # exibe o produto em formato json
]
