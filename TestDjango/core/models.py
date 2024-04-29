from django.db import models

# Create your models here.
class Persona(models.Model):
    
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    correo = models.EmailField()

    def __str__(self):
        return self.nombre
    
# Create your models here.
class Usuario(models.Model):
    run = models.IntegerField(primary_key=True, verbose_name='run', default=12345678)

    username = models.CharField(max_length=10, verbose_name='username', default='username_por_defecto')

    nombres = models.CharField(max_length=60, default='Nombre por defecto')

    apellidos = models.CharField(max_length=100, default='Apellido por defecto')

    
    password = models.CharField(max_length=255, default='password_por_defecto')

    perfil = models.IntegerField(null=True,blank=True,verbose_name='perfil')

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='movies/')

    def __str__(self):
        return self.title
