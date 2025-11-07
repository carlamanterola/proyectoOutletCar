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

class Coche(models.Model):
    matricula = models.CharField(max_length = 8)
    idMarca = models.ForeignKey(Marca, on_delete = models.CASCADE)
    idCat = models.ManyToManyField(Categoria)
    modelo = models.CharField(max_length = 50)
    anio = models.IntegerField(default = 0)
    km = models.IntegerField(default = 0)
    combustible = models.ManyToManyField(Combustible)
    precio = models.IntegerField(default = 0)

    def __str__(self):
        return f"{self.matricula} - {self.modelo}"