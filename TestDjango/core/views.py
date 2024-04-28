from django.shortcuts import render, redirect
from django.conf.urls.static import static
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Usuario
import requests

# Create your views here.
# Create your views here.
def iniciar_sesion(request):
    if request.method =='POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
        print("Datos del Form",username,password)
        #return render(request,'core/login_usuario.html')        
        usuarioBD = Usuario.objects.filter(username=username).first()
        print(usuarioBD)
        if usuarioBD is not None:
           if usuarioBD.password == password:
              if usuarioBD.perfil == 1:
                 print("Home administrador")
                 return redirect('home')
              if usuarioBD.perfil == 2:
                 print("Home Usuario")
                 return redirect('home')
              else:
                 print("No se encontrò perfil")
                 return render(request,'core/iniciar_sesion.html')
           else:
              print("Password Incorrecta")
              return render(request,'core/iniciar_sesion.html')
        else:
           print("Usuario no existe")
           return render(request,'core/iniciar_sesion.html')
    else:
      return render(request,'core/iniciar_sesion.html')

def home(request):
     return render(request, 'core/home.html')

def posts(request):
     return render(request, 'core/posts.html')


def detalle(request):
    return render(request, 'core/detalle.html')

def formulario(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['confirm_password']

        # Aquí puedes agregar más validaciones si lo necesitas
        if password == password_confirm:
            # Crea el usuario y lo guarda
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            messages.success(request, '¡Usuario registrado con éxito!')
            return redirect('home')
        else:
            messages.error(request, 'Las contraseñas no coinciden')
    return render(request, 'core/formulario.html')
#llamada de api
def form_api_back(request):
    url= "https://rickandmortyapi.com/api/character"
    response = requests.get(url)
    personajes = response.json().get('results',[])

    context = {
        'personajes' : personajes
    }
    return render(request, 'core/form_api_back.html',context)