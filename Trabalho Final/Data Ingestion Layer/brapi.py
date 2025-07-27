
import requests
import json

BASE_URL = "https://brapi.dev/api"
ENDPOINT = "/quote/PETR4"

API_KEY = "h5BphdNjnWU21ZAnJSjpDF" 

def get_stock_quote(ticker):
    url = f"{BASE_URL}{ENDPOINT.replace('PETR4', ticker)}"
    headers = {}
    if API_KEY:
        headers["Authorization"] = f"Bearer {API_KEY}" 

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar à brapi.dev: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON da brapi.dev: {e}")
        return None

if __name__ == "__main__":
    print("Testando a requisição para brapi.dev...")
    quote_data = get_stock_quote("VALE3") 
    if quote_data:
        print("Dados da cotação:")
        print(json.dumps(quote_data, indent=2))
    else:
        print("Não foi possível obter os dados da cotação.")
