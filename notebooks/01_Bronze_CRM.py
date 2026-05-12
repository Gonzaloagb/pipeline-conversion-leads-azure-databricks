# Databricks notebook source
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()


df_crm = spark.table("default.crm_leads")

display(df_crm)


df_crm.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("default.bronze_crm_leads")

df_bronze = spark.table("default.bronze_crm_leads")

display(df_bronze)

# COMMAND ----------

