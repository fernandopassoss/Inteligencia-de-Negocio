import requests
import json

BASE_URL = "https://servicodados.ibge.gov.br/api/v3/agregados"

AGREGADO = "1737" # Exemplo: IPCA - Índice Nacional de Preços ao Consumidor Amplo
PERIODOS = "last3" # Últimos 3 períodos
VARIAVEIS = "2266" # Exemplo: Variação mensal (%)

def get_ibge_data(agregado, periodos, variaveis):

    url = f"{BASE_URL}/{agregado}/periodos/{periodos}/variaveis/{variaveis}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar à API do IBGE: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON da API do IBGE: {e}")
        return None

if __name__ == "__main__":
    print("\nTestando a requisição para a API do IBGE...")
    ibge_data = get_ibge_data(AGREGADO, PERIODOS, VARIAVEIS)
    if ibge_data:
        print("Dados do IBGE (exemplo):")
        print(json.dumps(ibge_data, indent=2))
        if ibge_data and len(ibge_data) > 0 and 'resultados' in ibge_data[0]:
            for resultado in ibge_data[0]['resultados']:
                for serie in resultado['series']:
                    for localidade, valores in serie['serie'].items():
                        print(f"Localidade: {localidade}")
                        for periodo, valor in valores.items():
                            print(f"  Período: {periodo}, Valor: {valor}")
    else:
        print("Não foi possível obter os dados do IBGE.")


