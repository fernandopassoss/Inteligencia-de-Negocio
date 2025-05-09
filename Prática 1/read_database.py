import psycopg2
import time
import pandas as pd

time.sleep(5)

def connect_to_db():
    tentativa = 2
    while tentativa > 0:
        try:
            conn = psycopg2.connect(
                host="db",
                database="meubanco",
                user="postgres",
                password="senha_segura"
            )
            print("Conectado")
            return conn
        except psycopg2.OperationalError as e:
            tentativa -= 1
            print(f"Erro de conexão: {e}")
            time.sleep(2)

        raise Exception("Erro")

def fetch_data(conn, table_name):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()        
    columns = [desc[0] for desc in cursor.description]
    data = cursor.fetchall()
    cursor.close()

    return pd.DataFrame(data, columns=columns)
    
def main():
    conn = connect_to_db()
    table_name = "usuarios"
    
    for table in tables:
        print(f"\n --- Tabela {table} ---")
        df = fetch_data(conn, table)
        print(df)

while(1):
    main()