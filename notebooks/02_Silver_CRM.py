# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper, trim

spark = SparkSession.builder.getOrCreate()


df_bronze = spark.table("default.bronze_crm_leads")

display(df_bronze)



df_silver = df_bronze \
    .dropDuplicates() \
    .withColumn("nombre", upper(trim(col("nombre")))) \
    .withColumn("apellido", upper(trim(col("apellido")))) \
    .withColumn("email", trim(col("email"))) \
    .filter(col("email").isNotNull())

display(df_silver)

df_silver.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("default.silver_crm_leads")


df_verificacion = spark.table("default.silver_crm_leads")

display(df_verificacion)