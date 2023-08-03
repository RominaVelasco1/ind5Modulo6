from django.contrib import admin

# Register your models here.
from aplicacion_3.models import registroUsuarios

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'direccion', 'email', 'ciudad')


admin.site.register(registroUsuarios, UsuariosAdmin)
