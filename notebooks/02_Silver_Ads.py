# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper, trim

spark = SparkSession.builder.getOrCreate()


df_bronze_ads = spark.table("default.bronze_ads")


df_silver_ads = df_bronze_ads \
    .dropDuplicates() \
    .withColumn("canal", upper(trim(col("canal")))) \
    .withColumn("marca", upper(trim(col("marca")))) \
    .filter(col("campaign_id").isNotNull())

df_silver_ads.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("default.silver_ads")

df_verificacion = spark.table("default.silver_ads")

display(df_verificacion)