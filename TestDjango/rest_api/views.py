from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.responde import Response
from rest_framework.parsers import JSONParser
from rest_framework.authentification import TokenAuthentification
from rest_framework.permissions import IsAuthenticated 

# Create your views here.

@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))

@api_view(['POST'])
def login(request):
    
    data = JSONParser().parse(request)

    username = data['username']
    password = data['password']
    try:
        user = User.objects.get (username=username)
    except User.DoesNotExist:
        return Response("Usuario Incorrecto")

pass_valido = check_password(password, user.password)
if not pass_valido:
return Response ("Contraseña Incorrecta")

# recuperar el token
token, created = Token.objects.get_or_create(user=user)
return Response(token.key)