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
    matricula = models.CharField(max_length = 8, unique = True)
    idMarca = models.ForeignKey(Marca, on_delete = models.CASCADE, related_name ='marca')
    idCombustible = models.ForeignKey(Combustible, on_delete = models.CASCADE, related_name ='combustible')
    idPrecio = models.ForeignKey(Oferta, on_delete = models.SET_NULL, related_name ='oferta')
    idCat = models.ManyToManyField(Categoria, related_name ='categoria')
    
    modelo = models.CharField(max_length = 50)
    anio = models.IntegerField()
    km = models.IntegerField(null = True, blank = True)
    foto = models.ImageField(upload_to='fotos_coches/', null=True, blank=True)


    def __str__(self):
        return f"{self.matricula} - {self.modelo}"