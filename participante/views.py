from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import JsonResponse

def generar_arreglo(numero):
    if numero < 1:
        raise ValueError("El número debe ser mayor o igual a 1.")
    return list(range(1, numero + 1))


def organizar_torneo(numero_participantes):
    if numero_participantes < 1:
        raise ValueError("El número de participantes debe ser mayor o igual a 1.")

    array_p = generar_arreglo(numero_participantes)  # Generar el arreglo inicial de participantes
    num_grupos = (numero_participantes + 3) // 4  # Calcular la cantidad de grupos, redondeando hacia arriba
    grupos = [[] for _ in range(num_grupos)]  # Crear una lista vacía para cada grupo

    # Llenar los grupos con los participantes
    for i, participante in enumerate(array_p):
        grupos[i % num_grupos].append(participante)

    # Rellenar los grupos que queden incompletos con '0' (fantasmas)
    for grupo in grupos:
        while len(grupo) < 4:
            grupo.append(0)

    return array_p, grupos 


class Generar_Resultados(TemplateView):
    def get(self, request):
        try:
            numero_participantes = 25

            array_p, grupos = organizar_torneo(numero_participantes)

            contexto = {
                "numero_total_participantes": numero_participantes,
                "numero_grupos": len(grupos),
                "grupos": grupos,
                "array_p": array_p
            }

            return render(request, 'resultados.html', contexto)
        except ValueError as e:
            return render(request, 'resultados.html', {"error": str(e)})