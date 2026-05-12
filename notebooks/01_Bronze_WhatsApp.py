# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper, trim

spark = SparkSession.builder.getOrCreate()


df_bronze_whatsapp = spark.table("default.bronze_whatsapp")


df_silver_whatsapp = df_bronze_whatsapp \
    .dropDuplicates() \
    .withColumn("bot_name", upper(trim(col("bot_name")))) \
    .withColumn("intencion_detectada", upper(trim(col("intencion_detectada")))) \
    .filter(col("telefono").isNotNull())

df_silver_whatsapp.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("default.silver_whatsapp")

df_verificacion = spark.table("default.silver_whatsapp")

display(df_verificacion)