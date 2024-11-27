from django.urls import path
from . import views
from .views import Generar_Resultados

app_name='participantes'

urlpatterns = [
    path('generar-arreglo/', Generar_Resultados.as_view(), name='generar_arreglo'),
]
