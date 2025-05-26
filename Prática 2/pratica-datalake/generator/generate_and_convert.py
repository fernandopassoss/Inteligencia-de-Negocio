# generator/generate_and_convert.py
import os
import pandas as pd
import numpy as np # Usado para gerar dados mais variados

# O diretório de saída será montado como um volume no Docker Compose
output_dir = "/output_data"
os.makedirs(output_dir, exist_ok=True)

csv_file_path = os.path.join(output_dir, "one_million_rows.csv")
parquet_file_path = os.path.join(output_dir, "one_million_rows.parquet")
num_rows = 1_000_000

print(f"Iniciando geração do arquivo CSV com {num_rows} linhas em {csv_file_path}...")
# Gerando dados de exemplo
data = {
    'id': range(num_rows),
    'nome_produto': [f'Produto_{i}' for i in range(num_rows)],
    'preco': np.random.uniform(10.0, 500.0, num_rows).round(2),
    'quantidade': np.random.randint(1, 100, num_rows),
    'data_venda': pd.to_datetime('2024-01-01') + pd.to_timedelta(np.random.randint(0, 365 * 2, num_rows), unit='D')
}
df = pd.DataFrame(data)

df.to_csv(csv_file_path, index=False)
print(f"Arquivo CSV gerado com sucesso em {csv_file_path}.")

print(f"Iniciando conversão de CSV para Parquet em {parquet_file_path}...")
# Lê o CSV recém-criado e converte para Parquet
df_read_csv = pd.read_csv(csv_file_path)
df_read_csv.to_parquet(parquet_file_path, index=False, engine='pyarrow')
print(f"Arquivo Parquet gerado com sucesso em {parquet_file_path}.")

print(f"Tarefa do container 'generator' concluída. Arquivos estão em {output_dir}")