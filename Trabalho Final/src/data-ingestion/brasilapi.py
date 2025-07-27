import requests
import json

BASE_URL = "https://brasilapi.com.br/api"
ENDPOINT = "/feriados/v1/2025"

def get_bank_holidays(year):

    url = f"{BASE_URL}{ENDPOINT.replace('2025', str(year))}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar à BrasilAPI: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON da BrasilAPI: {e}")
        return None

if __name__ == "__main__":
    print("\nTestando a requisição para BrasilAPI...")
    holidays_2025 = get_bank_holidays(2025)
    if holidays_2025:
        print(f"Feriados bancários em 2025 ({len(holidays_2025)} feriados):")
        for i, holiday in enumerate(holidays_2025[:7]):
            print(f"- {holiday.get('name')} em {holiday.get('date')}")
    else:
        print("Não foi possível obter os feriados bancários.")


