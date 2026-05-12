# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import countDistinct, avg, col

spark = SparkSession.builder.getOrCreate()


df_crm = spark.table("default.silver_crm_leads")
df_whatsapp = spark.table("default.silver_whatsapp")
df_ads = spark.table("default.silver_ads")

df_whatsapp_sel = df_whatsapp.select(
    "lead_id",
    col("canal").alias("whatsapp_canal"),
    col("bot_name").alias("whatsapp_bot_name"),
    col("telefono").alias("whatsapp_telefono"),
    col("hora_inicio").alias("whatsapp_hora_inicio"),
    col("mensajes_usuario").alias("whatsapp_mensajes_usuario"),
    col("pregunta_frecuente").alias("whatsapp_pregunta_frecuente")
)


df_ads_sel = df_ads.select(
    "campaign_id",
    col("campaign_name").alias("ads_campaign_name"),
    col("canal").alias("ads_canal"),
    col("marca").alias("ads_marca"),
    col("inversion_ars").alias("ads_inversion_ars"),
    col("impresiones").alias("ads_impresiones"),
    col("clicks").alias("ads_clicks"),
    col("ctr_pct").alias("ads_ctr_pct"),
    col("cpc_ars").alias("ads_cpc_ars")
)


df_join_whatsapp = df_crm.join(
    df_whatsapp_sel,
    on="lead_id",
    how="left"
)


df_gold = df_join_whatsapp.join(
    df_ads_sel,
    on="campaign_id",
    how="left"
)


display(df_gold)

df_gold.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("default.gold_leads")


df_verificacion = spark.table("default.gold_leads")

display(df_verificacion)

# Total leads
display(
    df_gold.select(
        countDistinct("lead_id").alias("total_leads")
    )
)

display(
    df_gold.groupBy("canal_origen")
    .count()
)


display(
    df_gold.groupBy("provincia")
    .count()
)

display(
    df_gold.select(
        avg("score_interes").alias("promedio_score")
    )
)