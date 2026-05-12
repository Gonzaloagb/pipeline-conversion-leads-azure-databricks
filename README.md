# pipeline-conversion-leads-azure-databricks
Pipeline de Data Engineering con Azure Data Factory, Azure Data Lake y Databricks usando arquitectura Medallion.
# Azure Medallion Leads Pipeline

Proyecto de Ingeniería de Datos desarrollado con arquitectura Medallion utilizando Azure y Databricks.

## Objetivo

Integrar información de leads automotrices desde múltiples fuentes para generar métricas comerciales y KPIs de conversión.

## Tecnologías utilizadas

- Azure Data Factory
- Azure Data Lake Storage Gen2
- Azure Databricks
- PySpark
- Delta Lake
- Azure SQL Database
- REST API

## Arquitectura

Bronze → Silver → Gold

## Fuentes de datos

- crm.csv
- whatsapp_leads.csv
- campanias_ads.csv
- API dólar blue

## KPIs generados

- Leads por canal
- Leads por campaña
- Conversaciones WhatsApp
- Tasa de contacto
- CPC en USD
- Conversión por canal

## Automatización

Pipeline orquestado mediante Azure Data Factory con trigger diario.

## Autor

Gonzalo Blondi