from django.shortcuts import render, redirect
from django.conf.urls.static import static
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

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

def iniciar_sesion(request):
    if request.method == 'post':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrecta")
    return render(request, 'core/iniciar_sesion.html')
