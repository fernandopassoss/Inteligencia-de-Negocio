import pandas as pd
import numpy as np

data = {
    "coluna1": np.random.randint(0, 100, 10),
    "coluna2": np.random.random(10),
    "coluna3": np.random.choice(["A", "B", "C"], 10)
}

df = pd.DataFrame(data)

output_path = "/usr/src/app/dados/numeros_aleatorios.csv"
df.to_csv(output_path, index=False)

print(f"Arquivo CSV gerado em: {output_path}")