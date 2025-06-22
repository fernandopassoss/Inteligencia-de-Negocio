from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, avg, max, min
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType
import os

def create_spark_session():
    return SparkSession.builder \
        .appName("PySpark Container") \
        .config("spark.sql.adaptive.enabled", "true") \
        .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
        .getOrCreate()

def create_sample_data(spark):
    schema = StructType([
        StructField("id", IntegerType(), True),
        StructField("nome", StringType(), True),
        StructField("departamento", StringType(), True),
        StructField("salario", DoubleType(), True),
        StructField("idade", IntegerType(), True)
    ])

    data = [
        (1, "Ana Silva", "TI", 8500.0, 28),
        (2, "Carlos Santos", "RH", 6200.0, 35),
        (3, "Maria Oliveira", "TI", 9200.0, 31),
        (4, "João Costa", "Vendas", 7800.0, 29),
        (5, "Paula Lima", "TI", 8800.0, 26),
        (6, "Roberto Alves", "RH", 5900.0, 42),
        (7, "Fernanda Rocha", "Vendas", 7200.0, 33),
        (8, "Diego Martins", "TI", 9500.0, 30),
        (9, "Camila Ferreira", "Marketing", 6800.0, 27),
        (10, "Lucas Pereira", "Marketing", 7100.0, 32)
    ]

    return spark.createDataFrame(data, schema)

def analyze_data(df):
    df.show()

    # Estatísticas por departamento
    dept_stats = df.groupBy("departamento") \
        .agg(
            count("*").alias("total_funcionarios"),
            avg("salario").alias("salario_medio"),
            max("salario").alias("maior_salario"),
            min("salario").alias("menor_salario"),
            avg("idade").alias("idade_media")
        ) \
        .orderBy("salario_medio", ascending=False)

    dept_stats.show(truncate=False)

    salario_medio_geral = df.select(avg("salario")).collect()[0][0]
    print(f"Salário médio geral: {salario_medio_geral:.2f}")

    return dept_stats

def save_results(df, path="/app/output"):
    try:
        os.makedirs(path, exist_ok=True)
        df.coalesce(1) \
          .write \
          .mode("overwrite") \
          .parquet(f"{path}/departamento_stats.parquet")
    except Exception as e:
        print(f"Erro ao salvar: {e}")

def main():
    spark = create_spark_session()
    try:
        while True:
            df = create_sample_data(spark)
            dept_stats = analyze_data(df)
            save_results(dept_stats)
            
    except Exception as e:
        print(f"Erro durante execução: {e}")
    
    finally:
        spark.stop()
        print("Sessão Spark encerrada.")

if __name__ == "__main__":
    main()