from pyspark.sql import SparkSession
from pyspark.sql.functions import col, isnull
from pyspark.sql.types import StructType, StringType, DoubleType, LongType 

spark = SparkSession.builder \
    .appName("IoT Data Processing") \
    .config("spark.sql.parquet.compression.codec", "snappy") \
    .getOrCreate()

input_dir = "/data_input"
output_dir = "/data_lake/sensores"

schema = StructType() \
    .add("tipo", StringType(), True) \
    .add("cidade", StringType(), True) \
    .add("no2", StringType(), True) \
    .add("noise", StringType(), True) \
    .add("pm25", StringType(), True) \
    .add("pressao", LongType(), True) \
    .add("temp", DoubleType(), True) \
    .add("timestamp", StringType(), True) \
    .add("umidade", LongType(), True)

def process_data():
    
    df = spark.read.json(input_dir, multiLine=True, schema=schema) 

    print("Schema dos dados:")
    df.printSchema()

    df_filtrado = df.filter(
        ((col("tipo") == "clima") & (col("temp").isNotNull()) & (col("temp") > 20)) |
        ((col("tipo") == "smartcitizen") & (col("noise").isNotNull()) & (col("noise").cast("int") > 50))
    )

    print(f"Total de registros: {df.count()}")
    print(f"Registros filtrados: {df_filtrado.count()}")

    df_filtrado.write.mode("append") \
        .partitionBy("cidade") \
        .parquet(f"file://{output_dir}")

    print("Dados filtrados:")
    df_filtrado.show(truncate=False)

if __name__ == "__main__":
    while True:
        process_data()
        spark.streams.awaitAnyTermination(timeout=30)