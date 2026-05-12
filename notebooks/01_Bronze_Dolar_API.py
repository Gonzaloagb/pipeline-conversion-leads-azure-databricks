# Databricks notebook source
from pyspark.sql import SparkSession
import requests
import pandas as pd

spark = SparkSession.builder.getOrCreate()

url = "https://dolarapi.com/v1/dolares/blue"

response = requests.get(url)
data = response.json()

df_pandas = pd.DataFrame([data])

df_dolar = spark.createDataFrame(df_pandas)

display(df_dolar)

df_dolar.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("default.bronze_dolar_api")

df_verificacion = spark.table("default.bronze_dolar_api")

display(df_verificacion)