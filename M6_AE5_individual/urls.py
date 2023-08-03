
from django.contrib import admin
from django.urls import path
from aplicacion_3.views import primeraFuncion
from aplicacion_3.views import formularioContacto
from aplicacion_3.views import informeUsuarios
from aplicacion_3.views import user_login
from django.contrib.auth import views
#from django.contrib.auth.views import login, logout_then_login, LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', primeraFuncion, name = 'index'),
    path('registro/', formularioContacto, name = 'registro'),
    path('salida/', informeUsuarios, name = 'salida'),
    path('login/', user_login, name = 'login'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    
]

