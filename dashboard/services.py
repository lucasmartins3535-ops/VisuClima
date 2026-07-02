import requests
from datetime import datetime, timedelta

def obter_dados():
    agora = datetime.now()
    inicio = agora - timedelta(hours=24)

    url = "https://api.simepar.br/apigateway/api/consulta-dados-meteorologicos-por-estacao"

    headers = {
        "X-API-KEY": "DEFESA-D@DOS-2026"
    }

    params = {
        "estacoes": "23984834",
        "dataInicial": inicio.strftime("%Y-%m-%dT%H:%M:%S"),
        "dataFinal": agora.strftime("%Y-%m-%dT%H:%M:%S")
    }

    resposta = requests.get(
        url,
        headers=headers,
        params=params,
        verify=False
    )

    print("Status:", resposta.status_code)
    print("Headers:", resposta.headers)
    print("Resposta:", repr(resposta.text))

    if resposta.status_code == 200:
        return resposta.json()

    return None