from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView
from .models import Produto
from .forms import ProdutoForm


def produto_list(request):
    '''
    Trata uma requisição web e recupera os produtos renderizando em um html
    '''
    template_name = 'produto_list.html'
    objects = Produto.objects.all()
    search = request.GET.get('search')
    if search:
        objects = objects.filter(produto__icontains=search)
    context = {'object_list': objects}
    return render(request, template_name, context)


class ProdutoList(ListView):
    '''
    Exibe os produtos, a cada 10 registros
    '''
    model = Produto
    template_name = 'produto_list.html'
    paginate_by = 10

def produto_detail(request, pk):
    '''
    Permite a alteracao de um produto
    '''
    template_name = 'produto_detail.html'
    obj = Produto.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)


def produto_add(request):
    '''
    Trata uma requisição web e exibe um form para cadastro de produto
    '''
    template_name = 'produto_form.html'
    return render(request, template_name)


class ProdutoCreate(CreateView):
    '''
    Cria o form para adicao de novos produtos
    '''
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm


class ProdutoUpdate(UpdateView):
    '''
    Cria o form para alteracao produtos
    '''
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm


def produto_json(request, pk):
    ''' 
    Retorna o produto, id e quantidade. 
    '''
    produto = Produto.objects.filter(pk=pk)
    data = [item.to_dict_json() for item in produto]
    return JsonResponse({'data': data})


def save_data(data):
    '''
    Salva os dados no banco.
    '''
    aux = []
    for item in data:
        produto = item.get('produto')        
        disponivel = True if item.get('disponivel') == 'True' else False
        preco = item.get('preco')
        quantidade = item.get('quantidade')
        
        obj = Produto(
            produto=produto,            
            disponivel=disponivel,
            preco=preco,
            quantidade=quantidade,            
        )
        aux.append(obj)
    Produto.objects.bulk_create(aux)