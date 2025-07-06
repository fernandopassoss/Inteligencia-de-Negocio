import requests
import json
import time
import os
from datetime import datetime

os.makedirs("/data_input", exist_ok=True)

def get_sensor_value_safe(sensor_list, sensor_name):
    for sensor in sensor_list:
        if sensor.get("name") == sensor_name:
            return sensor.get("value")
    return None

def coletar_smartcitizen(kit_id=18774):
    url = f"https://api.smartcitizen.me/v0/devices/{kit_id}"
    r = requests.get(url)
    data = r.json()

    sensors_data = data.get('data', {}).get('sensors', [])

    leitura = {
        "tipo": "smartcitizen",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "no2": get_sensor_value_safe(sensors_data, "NO2"),
        "pm25": get_sensor_value_safe(sensors_data, "PM2.5"),
        "noise": get_sensor_value_safe(sensors_data, "Noise"),
        "temp": None,
        "umidade": None,
        "pressao": None,
        "cidade": None
    }

    nome_arquivo = f"/data_input/smartcitizen_{int(time.time())}.json"
    with open(nome_arquivo, 'w') as f:
        json.dump(leitura, f)
    print(f"Dados salvos: {nome_arquivo}")

def coletar_clima(api_key="a425d99b99b81966b141fac3cc83d887", cidade="Sidney"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric"
    r = requests.get(url)
    data = r.json()

    leitura = {
        "tipo": "clima",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "temp": data["main"]["temp"],
        "umidade": data["main"]["humidity"],
        "pressao": data["main"]["pressure"],
        "cidade": cidade,
        "no2": None,
        "pm25": None,
        "noise": None
    }

    nome_arquivo = f"/data_input/clima_{int(time.time())}.json"
    with open(nome_arquivo, 'w') as f:
        json.dump(leitura, f)
    print(f"Dados salvos: {nome_arquivo}")

if __name__ == "__main__":
    while True:
        try:
            coletar_smartcitizen()
            coletar_clima()
            time.sleep(30)
        except Exception as e:
            print(f"Erro: {e}")
            time.sleep(10)