from django.db import models

# Create your models here.
class Employee(models.Model):
    id        = models.AutoField    (primary_key=True)
    name      = models.CharField    (max_length=100)
    apellido1 = models.CharField    (max_length=100)
    apellido2 = models.CharField    (max_length=100)
    cargo     = models.CharField    (max_length=100)
    empresa   = models.CharField    (max_length=100)
    calle     = models.CharField    (max_length=100)
    numeroExt = models.IntegerField (default=1234)
    numeroInt = models.CharField    (max_length=10)
    colonia   = models.CharField    (max_length=100)
    municipio = models.CharField    (max_length=100)
    estado    = models.CharField    (max_length=100)
    codPos    = models.IntegerField (default=45060)
    telefono  = models.CharField(max_length=20) 
    email     = models.EmailField   (max_length=54)
    fechaNac  = models.DateField    (auto_now=False, auto_now_add=False)
    edad      = models.IntegerField (default=22)

    def __str__(self):
        texto = "Nombre: {0} \t Ocupación: ({1})"
        return texto.format(self.name, self.cargo)