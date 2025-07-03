import requests
import json
import time
import os

os.makedirs("/data_input", exist_ok=True)

def coletar_dado(kit_id=135):
    
        url = f"https://api.smartcitizen.me/v0/devices/{kit_id}"
        r = requests.get(url)
        data = r.json()

        for sensor in data['data']['sensors']:
                print(f"{sensor['name']}: {sensor['value']} {sensor['unit']}")

        leitura = {
                "timestamp": data["last_reading_at"],
                "temperature":next((d["value"] for d in data["data"]["sensors"] if d["name"] == "DHT22 - Temperature"), None),
                "humidity": next((d["value"] for d in data["data"]["sensors"] if d["name"] == "DHT22 - Humidity"), None),
                "solar": next((d["value"] for d in data["data"] if d["name"] == "Solar Panel"), None)
        }
        print(leitura)
        nome_arquivo = f"/data_input/leitura_{int(time.time())}.json"
        with open(nome_arquivo, 'w') as f:
            json.dump(leitura, f)

        print(f"Salvo: {nome_arquivo}")

if __name__ == "__main__":
    print("Iniciando o coletor de dados da Awesome API...")
    while True:
        try:
            coletar_dado()
            time.sleep(1)  
        except Exception as e:
            print(f"Erro ao coletar dados: {e}")
        