from .forms import OutlerCarModelForm
from django.shortcuts import render
from .models import Coche, Oferta

def formulario_coche(request):

    form = OutlerCarModelForm()
    context = {'form': form,}

    return render(request, 'form_coche.html', context)


def procesar_form_coche(request):
    from .forms import OutlerCarModelForm

    if(request.method == 'POST'):  #la unica diferencia entre GET y POST es que el GET se mando por url y POST por el body. Si en el html pones POST solo usas POST, por eso la opcion GET la borro aqui
        form = OutlerCarModelForm(request.POST, request.FILES)
        
        if (form.is_valid()):
            matricula = form.cleaned_data['matricula']
            marca = form.cleaned_data['idMarca']
            modelo = form.cleaned_data['modelo']
            anio = form.cleaned_data['anio']
            combustible = form.cleaned_data['idCombustible']
            categoria = form.cleaned_data['idCat']
            foto = form.cleaned_data['foto']
            km = form.cleaned_data['km']

            precio_valor = request.POST.get('precio')
            precio = Oferta(precio=precio_valor)
            precio.save()

            new_coche = Coche(matricula = matricula, idMarca = marca, modelo = modelo, anio = anio, idPrecio = precio, km = km, idCombustible = combustible, foto = foto)
            new_coche.save()

            new_coche.idCat.set(categoria)
            print(f"Nuevo coche guardado: \nMatricula: {matricula}, \nMarca: {marca}, \nModelo: {modelo}, \nAnio: {anio}, \nPrecio: {precio}, \nCombustible: {combustible}, \nCategoria: {categoria}")
            return render(request, 'form_coche.html', {'form': OutlerCarModelForm()})

        
        else:
            print(f"Errores del formulario: {form.errors}")
            return render(request, 'form_coche.html', {'form': form})
        
    else:
        form = OutlerCarModelForm()
        return render(request, 'form_coche.html', {'form': form})