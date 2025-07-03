from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType, DoubleType
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("SmartCitizen Streaming") \
    .getOrCreate()

schema = StructType() \
    .add("timestamp", StringType() ) \
    .add("temperature", DoubleType() ) \
    .add("humidity", DoubleType() ) \
    .add("solar", DoubleType())

df = spark.readStream \
    .schema(schema) \
    .json("/data_input")

df_filtrado = df.filter(col("temperature") > 30)

print(df_filtrado)

query = df_filtrado.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()