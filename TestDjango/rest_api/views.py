from django.shortcuts import render

# Create your views here.
#Contrucciòn del Rest
from rest_framework.response import Response
#Visualizaciòn del API Rest
from rest_framework.decorators import api_view
# Seguridad (Eliminar o activar)
from django.views.decorators.csrf import csrf_exempt
# Formato Json
from rest_framework.parsers import JSONParser
#libreria de còdigo de respuesta
from rest_framework import status

from core.models import Movie
from .serializers import MovieSerializer

from core.models import Persona
from .serializers import PersonaSerializer

##Librerìas de autenticaciòn  que se pueden comentar y no pedir la autorizacion##
from rest_framework.decorators import permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET','POST'])
#Librerìas de autenticaciòn  que se pueden comentar y no pedir la autorizacion##
@permission_classes((IsAuthenticated,))
def lista_persona(request):
    if request.method == 'GET':
        persona = Persona.objects.all()
        serializer = PersonaSerializer(persona,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PersonaSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            print('error',serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
@csrf_exempt
@api_view(['GET','POST'])
#@permission_classes((IsAuthenticated,))
def lista_Movie(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MovieSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
