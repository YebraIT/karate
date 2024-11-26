from django.contrib import admin
from .models import PerfilUsuario, PerfilUsuarioInline, Torneo
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

admin.site.register(PerfilUsuario)
admin.site.register(Torneo)

# Extender la clase del UserAdmin
class UserAdmin(BaseUserAdmin):
    inlines = (PerfilUsuarioInline,)

# Vuelve a registrar UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)