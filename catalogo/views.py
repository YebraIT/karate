from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Organizacion
# Vistas CRUD para Organizacion
class OrganizacionListView(ListView):
    model = Organizacion
    template_name = 'organizacion/organizacion_list.html'

class OrganizacionCreateView(CreateView):
    model = Organizacion
    fields = ['nombre', 'direccion', 'telefono', 'correo_electronico']
    template_name = 'organizacion/organizacion_form.html'
    success_url = reverse_lazy('organizacion_list')

class OrganizacionUpdateView(UpdateView):
    model = Organizacion
    fields = ['nombre', 'direccion', 'telefono', 'correo_electronico']
    template_name = 'organizacion/organizacion_form.html'
    success_url = reverse_lazy('organizacion_list')

class OrganizacionDeleteView(DeleteView):
    model = Organizacion
    template_name = 'organizacion/organizacion_confirm_delete.html'
    success_url = reverse_lazy('organizacion_list')

# Repite para Participante, Jugador, Torneo, etc.

