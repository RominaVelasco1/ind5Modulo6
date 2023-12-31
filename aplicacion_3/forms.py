from django import forms
from .models import registroUsuarios

class registroForm(forms.ModelForm):
    class Meta:
        model = registroUsuarios
        #fields = ['rut', 'nombre', 'apellido'] /// esto si quiero algunos campos. Alternativa, "all" 
        fields = '__all__'

class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=50, required=True, 
                              label="Nombre de usuario", 
                              error_messages={'required': 'Su nombre es requerido'})
    password = forms.CharField(widget=forms.PasswordInput, 
                               max_length=20, required=True, 
                               label="Contraseña", 
                               error_messages={'required': 'Contraseña es obligatoria'})
                               
