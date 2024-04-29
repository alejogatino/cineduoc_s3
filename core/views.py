from django.shortcuts import render
from django.conf.urls.static import static
import requests

# Create your views here.

def home(request):
     return render(request, 'core/home.html')

def posts(request):
     return render(request, 'core/posts.html')


def detalle(request):
    return render(request, 'core/detalle.html')

def formulario(request):
    return render(request, 'core/formulario.html')

def iniciar_sesion(request):
    return render(request, 'core/iniciar_sesion.html')

def datos_ingresados(request):
    username = request.GET.get('username')
    email = request.GET.get('email')
    password = request.GET.get('password')

    return render(request, 'formulario/datos_ingresados.html', {'username': username, 'email': email, 'password': password})

def api_auth_view(request):
    collection_id = 10  
    url = f'https://api.themoviedb.org/3/collection/{collection_id}/images'
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5YTk0NzViMDU1NzBjZmQ0MzBmYjljOTNmMmI1ZTBlNyIsInN1YiI6IjY2MmVkYzNkYTgwNjczMDEyOGU5MDY5MCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.hkYOtcYfZV_O_Mfghjbqlgil1KV7TWYm18uroFh97ug'
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    imagenes = []  
    context = {
        'imagenes': imagenes,
    }

    return render(request, 'nombre_de_tu_plantilla.html', context)

