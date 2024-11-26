from django.contrib.auth.models import User
from django.contrib import admin
from django.db import models

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    bio = models.TextField(blank=True, null=True)  # Ejemplo: biografía del usuario
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)  # Foto de perfil
    torneos = models.ManyToManyField('Torneo', blank=True, related_name='administradores')  # Relación de usuarios con torneos

    def __str__(self):
        return self.user.username
    
# Definir en línea para el perfil
class PerfilUsuarioInline(admin.StackedInline):
    model = PerfilUsuario
    can_delete = False
    verbose_name_plural = 'perfil'