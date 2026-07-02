from django.shortcuts import render
from django.http import JsonResponse
from .services import obter_dados

def home(request):
    dados = obter_dados()

    if dados:
        d = dados[0]

        dados = {
            "nomeEstacao": d["nomeEstacao"],
            "temperatura_media": d["Temperatura Média"],
            "temperatura_maxima": d["Temperatura Máxima"],
            "temperatura_minima": d["Temperatura Mínima"],
            "umidade_relativa": d["Umidade Relativa"],
            "pressao": d["Pressão"],
            "velocidade_vento": d["Velocidade do Vento"],
            "velocidade_rajada": d["Velocidade da Rajada"],
            "precipitacao": d["Precipitação"],
            "radiacao_solar": d["Radiação Solar"],
            "dataHora": d["dataHora"],
        }

    else:
        dados = {
            "nomeEstacao": "Sem conexão",
            "temperatura_media": "--",
            "temperatura_maxima": "--",
            "temperatura_minima": "--",
            "umidade_relativa": "--",
            "pressao": "--",
            "velocidade_vento": "--",
            "velocidade_rajada": "--",
            "precipitacao": "--",
            "radiacao_solar": "--",
            "dataHora": "--",
        }

    return render(request, "dashboard/home.html", {"dados": dados})

def api_temperatura(request):
    dados = obter_dados()

    lista = []

    for d in dados:
        lista.append({
            "dataHora": d["dataHora"],
            "temperatura_media": d["Temperatura Média"]
        })

    return JsonResponse(lista, safe=False)