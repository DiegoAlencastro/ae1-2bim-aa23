from django.db import models

# Creacion de modelos a usar
class Restaurante(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    estrellas = models.IntegerField()
    numero_surcursales = models.IntegerField()
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return """Nombre: %s \n 
                Direccion: %s \n
                Numero de estrellas: %d \n
                Numero de sucursales: %d \n
                Telefono: %s \n
                """ % (self.nombre,self.direccion, self.estrellas, self.numero_surcursales, self.telefono)