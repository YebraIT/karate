from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import JsonResponse
from django.db.models import Q
from torneo.models import VW_Jugador, Torneo,VW_Grupos_Division_Kata, VW_Grupos_Division_Kumite, VW_Grupos_Concentrado_Kata, VW_Grupos_Concentrado_Kumite

def organizar_torneo_por_categoria(jugadores, categoria):
    # Filtrar jugadores por la categoría
    jugadores_categoria = jugadores.filter(
        tipo_id=categoria['tipo_id'], sexo=categoria['sexo']
    ).values('id', 'nombre', 'paterno')  # Obtener id, nombre y paterno

    numero_participantes = len(jugadores_categoria)
    if numero_participantes < 1:
        return [], []  # Sin jugadores para esta categoría
    
    else:
        num_grupos = (numero_participantes + 3) // 4  # Calcular cantidad de grupos
        grupos = [[] for _ in range(num_grupos)]

        # Asignar jugadores a los grupos y numerarlos dentro de cada grupo
        numero_global = 1

        for i, jugador in enumerate(jugadores_categoria):
            # Asignamos el jugador con el número local al grupo
            jugador_con_numero = jugador.copy()
            grupo_idx = i % num_grupos
            jugador_con_numero['numero'] = (len(grupos[grupo_idx]) + 1)  # Numeración interna dentro del grupo
            grupos[grupo_idx].append(jugador_con_numero)
            numero_global += 1  # Incrementar el número global para el siguiente jugador

        # Completar los grupos con fantasmas y mantener la numeración
        for grupo in grupos:
            while len(grupo) < 4:
                grupo.append({'id': 0, 'nombre': 'Fantasma', 'paterno': '', 'numero': len(grupo) + 1})

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
            #KATA
            jugadores_kata = VW_Jugador.objects.filter(Q(competencia_id=1) | Q(competencia_id=3))
            division_kata = VW_Grupos_Division_Kata.objects.values(
                'tipo_id', 'Categoria', 'sexo'
            )

            grup_division_kata = []

            for dato in division_kata:
                array_p, grupos = organizar_torneo_por_categoria(jugadores_kata, dato)
                grup_division_kata.append({
                    "Categoria": dato['Categoria'],
                    "sexo": dato['sexo'],
                    "numero_total_participantes": len(array_p),
                    "numero_grupos": len(grupos),
                    "grupos": grupos,
                })

            #KUMITE
            jugadores_kumite = VW_Jugador.objects.filter(Q(competencia_id=2) | Q(competencia_id=3))
            division_kumite = VW_Grupos_Division_Kumite.objects.values(
                'tipo_id', 'Categoria', 'sexo'
            )

            grup_division_kumite = []

            for dato in division_kumite:
                array_p, grupos = organizar_torneo_por_categoria(jugadores_kumite, dato)
                grup_division_kumite.append({
                    "Categoria": dato['Categoria'],
                    "sexo": dato['sexo'],
                    "numero_total_participantes": len(array_p),
                    "numero_grupos": len(grupos),
                    "grupos": grupos,
                })

            all_grup = []
            all_grup.extend(grup_division_kata)
            all_grup.extend(grup_division_kumite)
            print(all_grup)
            tatamis = [[], [], []]
            for grupo in all_grup:
                for subgrupo in grupo['grupos']:
                    # Encuentra el tatami con menos subgrupos y asigna el subgrupo allí
                    tatami_index = min(range(3), key=lambda i: len(tatamis[i]))
                    tatamis[tatami_index].append({
                        "Categoria": grupo['Categoria'],
                        "sexo": grupo['sexo'],
                        "subgrupo": subgrupo
                    })

            contexto = {
                'torneos_list': torneos_list,
                'grup_division_kata':grup_division_kata,
                'grup_division_kumite': grup_division_kumite,
                'tatamis': tatamis,
            }

            return render(request, 'resultados.html', contexto)
        except ValueError as e:
            return render(request, 'resultados.html', {"error": str(e)})

