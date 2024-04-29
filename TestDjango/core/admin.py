from django.contrib import admin
from .models import Persona, Usuario, Movie
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Persona)
admin.site.register(Movie)