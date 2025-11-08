from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Marca, Categoria, Combustible, Oferta, Coche

# Página principal [PLACEHOLDER]
def index(request):
    return HttpResponse('PÁGINA PRINCIPAL :P')

# Devuelve una lista de ofertas
def index_ofertas(request):
    ofertas = get_list_or_404(Oferta)
    context = {'lista_ofertas': ofertas}
    return render(request, 'ofertas.html', context)

# Devuelve los detalles de una oferta en concreto según ID
def ver_oferta(request, idOferta):
    oferta = get_object_or_404(Oferta, pk=idOferta)
    context = {'oferta': oferta}
    return render(request, 'oferta.html', context)