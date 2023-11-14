from django.db import models

# Create your models here.
# Usuario necesita Nombre, Password, Email
class Usuario(models.Model):
    Nombre = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    
    def __str__(self):
        return self.Nombre



#La receta necesita: Categoria,Nombre,Ingredientes,Preparacion, Calificacion, Autor
class Receta(models.Model):
    Categoria = models.CharField(max_length=255)
    Nombre = models.CharField(max_length=255)
    Ingredientes = models.TextField()
    Preparacion = models.TextField()
    Calificacion = models.IntegerField(max_length=5)
    Autor = models.IntegerField()
    
    def __str__(self):
        return self.Nombre
