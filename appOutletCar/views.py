from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Marca, Categoria, Oferta, Coche, Combustible



###### VIEWS ACCESIBLES PARA TODOS ######
def index(request):
    coche = get_object_or_404(Coche, matricula="3406 GNV")
    return render(request, 'index.html', {'coche': coche})

# Devuelve una lista de ofertas
def index_ofertas(request):
    ofertas = get_list_or_404(Oferta)
    context = {'lista_ofertas': ofertas}
    return render(request, 'lista_ofertas.html', context)

# Devuelve los detalles de una oferta en concreto según ID
def ver_oferta(request, idOferta):
    oferta = get_object_or_404(Oferta, pk=idOferta)
    coche = oferta.oferta
    context = {'oferta': oferta, 'coche': coche}
    return render(request, 'detalle_oferta.html', context)


#Visualizar la lista de marcas
def visualizar_marcas(request):
    marcas = get_list_or_404(Marca)
    context = {"marcas": marcas}
    return render(request, "lista_marcas.html", context)

#Visualizar los coches de una marca en concreto segun ID
def ver_marca(request, idMarca):
    #marcas = Marca.objects.get(id=idMarca)
    marcas = get_object_or_404(Marca, id=idMarca)
    coches = get_list_or_404(Coche, idMarca_id=idMarca)
    context = {"coches": coches, "idMarca": idMarca, "marca": marcas}
    return render(request, "detalle_marca.html", context)

#Visualizar la lista de categorias
def lista_categorias(request):
    categorias = get_list_or_404(Categoria)
    context = {'categorias': categorias}
    return render(request, 'lista_categorias.html', context)

#Visualizar los coches de una categoria en concreto segun ID
def detalle_categoria(request, idCat):
    categoria = get_object_or_404(Categoria, pk=idCat)
    coches = Coche.objects.filter(idCat=categoria)
    context = {'categoria': categoria, 'coches': coches}
    return render(request, 'detalle_categoria.html', context)

# Página principal que muestra el coche más barato por cada marca
def index(request):
    marcas = Marca.objects.all()
    coches_por_marca = [] 

    for marca in marcas:
        coches = Coche.objects.filter(idMarca=marca, idPrecio__isnull=False)
        if coches.exists():
            coche_mas_barato = coches.order_by('idPrecio__precio').first()
            coches_por_marca.append(coche_mas_barato)

    return render(request, 'index.html', {'coches': coches_por_marca})

def combustible(request, idCombustible):
    combustible = get_object_or_404(Combustible, pk=idCombustible)
    coches = Coche.objects.filter(idCombustible=combustible)
    return render(request, 'detalle_combustible.html', {'combustible': combustible, 'coches': coches})


def eliminar_coche(request, pk):
    coche = get_object_or_404(Coche, pk=pk)

    if request.method == 'POST':
        coche.delete()        
        return redirect(reverse('index')) 

    context = {
        'object': coche,
    }
    return render(request, 'eliminar_coche.html', context)