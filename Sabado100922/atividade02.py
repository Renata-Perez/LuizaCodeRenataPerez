import requests

def ler_cotacao_dolar():
    url = "https://economia.awesomeapi.com.br:443/json/last/USD-BRL"
    resposta_web = requests.get(url)

    if not resposta_web.ok:
        return None
    
    resposta_json = resposta_web.json()
    return resposta_json

def obter_valor_dolar(cotacao_web):
    valor_dolar = cotacao_web["USDBRL"]["bid"]
    return valor_dolar


def principal():
    cotacao_web = ler_cotacao_dolar()
    valor_dolar = obter_valor_dolar(cotacao_web)
    print("Valor do dólar ", valor_dolar)


if __name__ == "__main__":
    principal()