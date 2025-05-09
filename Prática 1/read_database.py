import psycopg2
import time
import pandas as pd


time.sleep(5)

def read_csv_file():
    file_path = "/usr/src/app/dados/numeros_aleatorios.csv"
    try:
        df = pd.read_csv(file_path)
        print("\n--- Conteúdo do arquivo CSV ---")
        print(df)
    except FileNotFoundError:
        print(f"Arquivo {file_path} não encontrado.")

def connect_to_db():
    tentativas = 2
    while tentativas > 0:
        try:
            conn = psycopg2.connect(
                host="db",
                database="meubanco",
                user="postgres",
                password="senha_segura"
            )
            print("Conectado ao banco de dados.")
            return conn
        except psycopg2.OperationalError as e:
            tentativas -= 1
            print(f"Erro de conexão: {e}. Tentativas restantes: {tentativas}")
            time.sleep(2)
    
    raise Exception("Não foi possível conectar ao banco de dados após várias tentativas.")

def fetch_data(conn, table_name):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()        
    columns = [desc[0] for desc in cursor.description]
    cursor.close()

    return pd.DataFrame(rows, columns=columns)

def main():
    conn = connect_to_db()
    tables = ['usuarios']
    
    for table in tables:
        print(f"\n--- Dados da tabela {table} ---")
        df = fetch_data(conn, table)
        print(df)
    

    read_csv_file()

while True:
    main()
    time.sleep(10)  