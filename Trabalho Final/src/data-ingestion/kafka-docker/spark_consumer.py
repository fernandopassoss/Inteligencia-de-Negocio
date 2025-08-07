from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, DoubleType

# Cria uma sessão Spark
spark = SparkSession.builder \
    .appName("KafkaSparkConsumer") \
    .master("local[*]") \
    .config("spark.kafka.bootstrap.servers", "kafka:9092") \
    .getOrCreate()

# Define o schema dos dados esperados (ajuste conforme o retorno da brapi)
schema = StructType() \
    .add("symbol", StringType()) \
    .add("longName", StringType()) \
    .add("regularMarketPrice", DoubleType()) \
    .add("currency", StringType()) \
    .add("regularMarketTime", StringType()) \
    .add("regularMarketChange", DoubleType())

# Lê do Kafka
df_kafka_raw = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "mercado_financeiro") \
    .option("startingOffsets", "latest") \
    .load()

# Converte os dados de value (binário) para JSON
df_com_dados = df_kafka_raw.selectExpr("CAST(value AS STRING) as json_str") \
    .select(from_json(col("json_str"), schema).alias("dados")) \
    .select("dados.*")

# Mostra no console
query = df_com_dados.writeStream \
    .outputMode("append") \
    .format("console") \
    .option("truncate", False) \
    .start()

query.awaitTermination()
