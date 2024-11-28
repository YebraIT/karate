from django.urls import path
#from rest_framework import routers
from .views import (
    JugadorCreateView, JugadorDeleteView, JugadorDetailView, JugadorListView, JugadorUpdateView, ParticipanteListView, ParticipanteCreateView, ParticipanteUpdateView,
    ParticipanteDeleteView, ParticipanteDetailView, generar_gafete,
    # Importa las vistas para los otros modelos aquí...
)

app_name='torneos'
#router=routers.DefaultRouter()
urlpatterns = [
    path('participantes/', ParticipanteListView.as_view(), name='participante_list'),
    path('participantes/new/', ParticipanteCreateView.as_view(), name='participante_create'),
    path('participantes/<int:pk>/edit/', ParticipanteUpdateView.as_view(), name='participante_update'),
    path('participantes/<int:pk>/delete/', ParticipanteDeleteView.as_view(), name='participante_delete'),
    path('participantes/<int:pk>/', ParticipanteDetailView.as_view(), name='participante_detail'),
    # Agrega rutas para los otros modelos...
    path('jugadores/', JugadorListView.as_view(), name='jugador_list'),
    path('jugadores/new/', JugadorCreateView.as_view(), name='jugador_create'),
    path('jugadores/<int:pk>/edit/', JugadorUpdateView.as_view(), name='jugador_update'),
    path('jugadores/<int:pk>/delete/', JugadorDeleteView.as_view(), name='jugador_delete'),
    path('jugadores/<int:pk>/', JugadorDetailView.as_view(), name='jugador_detail'),
    path('jugadores/', JugadorListView.as_view(), name='jugador_list'),
    path('jugadores/<int:jugador_id>/gafete/', generar_gafete, name='gafete_jugador'),

]