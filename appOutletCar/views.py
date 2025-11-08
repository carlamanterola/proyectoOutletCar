from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Marca, Categoria, Combustible, Coche


def index_coches(request):
    coches = get_list_or_404(Coche)
    output =  ', '.join([c.modelo for c in coches])
    return HttpResponse(output)
