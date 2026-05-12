# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, round

spark = SparkSession.builder.getOrCreate()


df_gold = spark.table("default.gold_leads")

df_dolar = spark.table("default.silver_dolar_api")

display(df_gold)
display(df_dolar)


valor_dolar = df_dolar.select("venta").first()[0]

print(f"Valor dólar blue: {valor_dolar}")

df_gold_conversion = df_gold \
    .withColumn(
        "cpc_usd",
        round(col("ads_cpc_ars") / valor_dolar, 2)
    ) \
    .withColumn(
        "inversion_usd",
        round(col("ads_inversion_ars") / valor_dolar, 2)
    )

df_gold_conversion.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("default.gold_leads_conversion")


df_verificacion = spark.table("default.gold_leads_conversion")

display(df_verificacion)

display(
    df_gold_conversion.selectExpr(
        "count(distinct lead_id) as total_leads"
    )
)

display(
    df_gold_conversion.groupBy("canal_origen")
    .count()
)


display(
    df_gold_conversion.groupBy("provincia")
    .count()
)

display(
    df_gold_conversion.selectExpr(
        "avg(score_interes) as promedio_score"
    )
)

display(
    df_gold_conversion.selectExpr(
        "avg(cpc_usd) as promedio_cpc_usd"
    )
)