from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import JsonResponse
from torneo.models import VW_Jugador, Torneo

def organizar_torneo_por_categoria(jugadores, categoria):
    jugadores_categoria = jugadores.filter(
        categoria=categoria['categoria'], sexo=categoria['sexo']
    ).values_list('id', flat=True)

    numero_participantes = len(jugadores_categoria)
    if numero_participantes < 1:
        return [], []  # Sin jugadores para esta categoría

    num_grupos = (numero_participantes + 3) // 4  # Calcular cantidad de grupos
    grupos = [[] for _ in range(num_grupos)]

    # Llenar los grupos con jugadores
    for i, jugador in enumerate(jugadores_categoria):
        grupos[i % num_grupos].append(jugador)

    # Completar los grupos con ceros si hay menos de 4 participantes
    for grupo in grupos:
        while len(grupo) < 4:
            grupo.append(0)

    return list(jugadores_categoria), grupos

class Generar_Resultados(TemplateView):
    def get(self, request):
        try:
            torneos_list = Torneo.objects.all()

            contexto = {
                'torneos_list': torneos_list,
            }

            return render(request, 'resultados.html', contexto)
        except ValueError as e:
            return render(request, 'resultados.html', {"error": str(e)})

    def post(self, request):
        try:
            torneos_list = Torneo.objects.all()
            jugadores = VW_Jugador.objects.all()
            categorias = VW_KATA.objects.values(
                'id_cat', 'categoria', 'sexo'
            ).distinct()

            resultados_por_categoria = []

            for categoria in categorias:
                array_p, grupos = organizar_torneo_por_categoria(jugadores, categoria)
                resultados_por_categoria.append({
                    "categoria": categoria['categoria'],
                    "sexo": categoria['sexo'],
                    "numero_total_participantes": len(array_p),
                    "numero_grupos": len(grupos),
                    "grupos": grupos,
                })

            contexto = {
                'torneos_list': torneos_list,
                'resultados_por_categoria': resultados_por_categoria,
            }

            return render(request, 'resultados.html', contexto)
        except ValueError as e:
            return render(request, 'resultados.html', {"error": str(e)})
