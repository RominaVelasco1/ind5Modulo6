from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from aplicacion_3.models import registroUsuarios
from .forms import registroForm, LoginForm
from django.contrib import messages

# CLIENTES
def primeraFuncion(request):
    return render(request, 'landing.html')

def formularioContacto(request):
    data = {
        'form': registroForm()
    }
    if request.method == 'POST':
        formulario = registroForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "CLIENTE REGISTRADO !!!"
        else:
            data["form"] = formulario
    return render(request, 'registro.html', data)

def informeUsuarios(request):
     #'usuarios' es una instancia de la clase "registroUsuarios" definida en models.py
    usuarios = registroUsuarios.objects.all()
    return render(request, 'salida.html', {'usuarios': usuarios})
##############################################################################################

# USUARIOS
def user_login(request):
    
    if request.method == 'POST':
        formulario = LoginForm(data=request.POST)
        if formulario.is_valid():
           usuario = formulario.cleaned_data['usuario']
           password = formulario.cleaned_data['password']
           user = authenticate(request, username=usuario, password=password)
           if user is not None:
               if user.is_active:
                   login(request, user)
                   messages.success(request, f"Autentificación exitosa, estimado(a) {usuario}")
                   return render(request, 'landing.html')
                   #return HttpResponse(f"Autentificación exitosa, estimado(a) {usuario}")
               else:
                   messages.error(request, "Cuenta no habilitada")
                   #return HttpResponse("Cuenta NO habilitada")
           else:
               #return HttpResponse("Login No válido")
                messages.error(request, "Login no válido")
    else:
        formulario = LoginForm()

    return render(request, 'registration/login.html', {'formulario': formulario})
