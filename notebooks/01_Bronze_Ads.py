# Databricks notebook source
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()


df_ads = spark.table("default.ads_leads")

display(df_ads)


df_ads.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("default.bronze_ads")

df_bronze_ads = spark.table("default.bronze_ads")

display(df_bronze_ads)