from rest_framework import serializers
from core.models import Persona, Movie



class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'image']

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['nombre', 'edad', 'correo']