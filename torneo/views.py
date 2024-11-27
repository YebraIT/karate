from django.shortcuts import render
from torneo.models import Clasificacion
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Participante, Jugador, Torneo, Organizacion, Categoria, TipoParticipante, ParticipacionTorneo, Clasificacion

# Create your views here.
def actualizar_clasificacion(partido):
    clas_local = Clasificacion.objects.get(participante=partido.equipo_local, torneo=partido.torneo)
    clas_visitante = Clasificacion.objects.get(participante=partido.equipo_visitante, torneo=partido.torneo)

    # Actualizar estadísticas del equipo local
    clas_local.partidos_jugados += 1
    clas_local.goles_a_favor += partido.resultado_local
    clas_local.goles_en_contra += partido.resultado_visitante
    clas_local.diferencia_goles = clas_local.goles_a_favor - clas_local.goles_en_contra

    # Actualizar estadísticas del equipo visitante
    clas_visitante.partidos_jugados += 1
    clas_visitante.goles_a_favor += partido.resultado_visitante
    clas_visitante.goles_en_contra += partido.resultado_local
    clas_visitante.diferencia_goles = clas_visitante.goles_a_favor - clas_visitante.goles_en_contra

    # Definir quién ganó o si fue empate
    if partido.resultado_local > partido.resultado_visitante:
        clas_local.victorias += 1
        clas_local.puntos += 3
        clas_visitante.derrotas += 1
    elif partido.resultado_local < partido.resultado_visitante:
        clas_visitante.victorias += 1
        clas_visitante.puntos += 3
        clas_local.derrotas += 1
    else:
        clas_local.empates += 1
        clas_visitante.empates += 1
        clas_local.puntos += 1
        clas_visitante.puntos += 1

    clas_local.save()
    clas_visitante.save()


# Vistas para Participante
class ParticipanteListView(ListView):
    model = Participante
    template_name = 'participante/participante_list.html'

class ParticipanteCreateView(CreateView):
    model = Participante
    fields = '__all__'
    template_name = 'participante/participante_form.html'
    success_url = reverse_lazy('participante_list')

class ParticipanteUpdateView(UpdateView):
    model = Participante
    fields = '__all__'
    template_name = 'participante/participante_form.html'
    success_url = reverse_lazy('participante_list')

class ParticipanteDeleteView(DeleteView):
    model = Participante
    template_name = 'participante/participante_confirm_delete.html'
    success_url = reverse_lazy('participante_list')

class ParticipanteDetailView(DetailView):
    model = Participante
    template_name = 'participante/participante_detail.html'

# Replicar las vistas para los demás modelos (Jugador, Torneo, etc.)

# Vistas para Participante
class JugadorListView(ListView):
    model = Jugador
    template_name = 'jugador/jugador_list.html'

class JugadorCreateView(CreateView):
    model = Jugador
    fields = '__all__'
    template_name = 'jugador/jugador_form.html'
    success_url = reverse_lazy('jugador_list')

class JugadorUpdateView(UpdateView):
    model = Jugador
    fields = '__all__'
    template_name = 'jugador/jugador_form.html'
    success_url = reverse_lazy('torneos:jugador_list')

class JugadorDeleteView(DeleteView):
    model = Jugador
    template_name = 'jugador/jugador_confirm_delete.html'
    success_url = reverse_lazy('torneos:jugador_list')

class JugadorDetailView(DetailView):
    model = Jugador
    template_name = 'jugador/jugador_detail.html'