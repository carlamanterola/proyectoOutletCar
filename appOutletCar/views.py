from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Marca, Categoria, Oferta, Coche, Combustible, Favorito
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
import random


###### VIEWS ACCESIBLES PARA TODOS ######


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


####################### TEMPORAL, PROBABLEMENTE SE CAMBIE
@login_required
def agregar_favorito(request, coche_id):
    coche = get_object_or_404(Coche, id=coche_id)
    Favorito.objects.get_or_create(usuario=request.user, coche=coche)
    return redirect(request.META.get("HTTP_REFERER", "lista_favoritos"))

@login_required
def lista_favoritos(request):
    favoritos = Favorito.objects.filter(usuario=request.user).select_related("coche")
    return render(request, "lista_favoritos.html", {"favoritos": favoritos})


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


def index(request):
    return render(request, 'index.html')

def coches_mas_baratos_json(request):
    marcas = Marca.objects.all()
    resultado = []

    for marca in marcas:
        coches = Coche.objects.filter(idMarca=marca, idPrecio__isnull=False)
        if coches.exists():
            coche = coches.order_by('idPrecio__precio').first()

            resultado.append({
                "marca_id": marca.id,
                "marca_nombre": marca.nomMarca,
                "modelo": coche.modelo, 
                "precio": coche.idPrecio.precio,
                "oferta_id": coche.idPrecio.id,
                "foto": coche.foto.url if coche.foto else None,
            })

    return JsonResponse(resultado, safe=False)


def combustible(request, idCombustible):
    combustible = get_object_or_404(Combustible, pk=idCombustible)
    coches = Coche.objects.filter(idCombustible=combustible)
    return render(request, 'detalle_combustible.html', {'combustible': combustible, 'coches': coches})

@staff_member_required
def eliminar_coche(request, pk):
    coche = get_object_or_404(Coche, pk=pk)

    if request.method == 'POST':
        coche.delete()        
        return redirect(reverse('index')) 

    context = {
        'object': coche,
    }
    return render(request, 'eliminar_coche.html', context)


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")

        return render(request, "login.html", {
            "error": "Usuario o contraseña incorrectos"
        })

    return render(request, "login.html")


def index(request):
    coches = Coche.objects.exclude(foto='')

    cocheAleatorio = random.choice(coches) if coches.exists() else None

    context = {
        "cocheAleatorio": cocheAleatorio
    }

    return render(request, "index.html", context)