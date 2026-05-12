# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date

spark = SparkSession.builder.getOrCreate()

df_dolar = spark.table("default.bronze_dolar_api")

display(df_dolar)


df_silver_dolar = df_dolar \
    .withColumn(
        "fecha_actualizacion",
        to_date(col("fechaActualizacion"))
    ) \
    .dropDuplicates()

display(df_silver_dolar)


df_silver_dolar.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("default.silver_dolar_api")


df_verificacion = spark.table("default.silver_dolar_api")

display(df_verificacion)