from django.db import models

class Marca(models.Model):
    nomMarca = models.CharField(max_length = 50)

    def __str__(self):
        return self.nomMarca


class Categoria(models.Model):
    nomCat = models.CharField(max_length = 50)

    def __str__(self):
        return self.nomCat

class Combustible(models.Model):
    nomCombustible = models.CharField(max_length = 50)

    def __str__(self):
        return self.nomCombustible
    
class Oferta(models.Model):
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.precio} €"

class Coche(models.Model):
    matricula = models.CharField(max_length = 8)
    idMarca = models.ForeignKey(Marca, on_delete = models.CASCADE)
    idCombustible = models.ForeignKey(Combustible, on_delete=models.CASCADE)
    idPrecio = models.OneToOneField(Oferta, on_delete=models.SET_NULL, null=True, blank = True)
    idCat = models.ManyToManyField(Categoria)
    
    modelo = models.CharField(max_length = 50)
    anio = models.IntegerField()
    km = models.IntegerField()

    def __str__(self):
        return f"{self.matricula} - {self.modelo}"