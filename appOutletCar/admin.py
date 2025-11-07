from django.contrib import admin
from .models import Marca, Categoria, Combustible, Coche

# Register your models here.
admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Combustible)
admin.site.register(Coche)