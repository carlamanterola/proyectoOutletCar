from django import forms
from .models import Coche, Oferta, Categoria

class OutlerCarModelForm(forms.ModelForm):
    class Meta:
        model = Coche
        fields = ['matricula', 'idMarca','modelo', 'anio', 'km', 'idCombustible', 'idCat', 'foto']


        

        widgets = {
            'idCat': forms.CheckboxSelectMultiple(),
        }