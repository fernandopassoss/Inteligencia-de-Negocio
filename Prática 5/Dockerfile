FROM python:3.9-slim

ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
ENV PYSPARK_PYTHON=python3

RUN apt-get update && apt-get install -y \
    default-jdk \
    wget \
    curl \
    procps \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ARG SPARK_VERSION=3.4.1
ARG HADOOP_VERSION=3

RUN wget -q "https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" \
    && tar xzf "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" -C /opt/ \
    && mv "/opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}" "$SPARK_HOME" \
    && rm "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz"

RUN pip install --no-cache-dir \
    pyspark==3.4.1 \
    py4j

WORKDIR /app
COPY app.py /app/
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /app/output

EXPOSE 4040 4041 8080 8081

RUN useradd -m -u 1000 sparkuser && chown -R sparkuser:sparkuser /app
USER sparkuser

CMD ["python", "app.py"]