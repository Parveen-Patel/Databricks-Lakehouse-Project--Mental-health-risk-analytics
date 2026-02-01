# Databricks notebook source


# COMMAND ----------

# MAGIC %md
# MAGIC Mental health risk is not caused by one factor alone. Users with high screen time, reduced sleep and late-night usage show the highest depression and anxiety. This demonstrates a compounding behavioral risk effect.

# COMMAND ----------

# DBTITLE 1,Behavioral Risk Combination
display(spark.sql("""
SELECT *
FROM ecommerce.mental_health.gold_behavioral_risk_patterns
ORDER BY Risk_Percentage DESC
LIMIT 10
"""))


# COMMAND ----------

# MAGIC %md
# MAGIC Exposure to comparison-driven content significantly increases anxiety levels, highlighting the psychological cost of curated social feeds.

# COMMAND ----------

# DBTITLE 1,Social Comparison Effect
display(spark.sql("""
SELECT 
    Social_Comparison_Risk,
    AVG(High_Mental_Health_Risk) AS Risk_Rate
FROM ecommerce.mental_health.silver_user_features
GROUP BY Social_Comparison_Risk
"""))

# COMMAND ----------

# MAGIC %md
# MAGIC High screen time users show elevated mental distress, supporting research linking digital overexposure to emotional fatigue.

# COMMAND ----------

# DBTITLE 1,Screen Time vs Depression Trend
display(spark.sql("""
SELECT 
    High_Screen_Time,
    AVG(High_Mental_Health_Risk) AS Risk_Rate
FROM ecommerce.mental_health.silver_user_features
GROUP BY High_Screen_Time
"""))


# COMMAND ----------

# MAGIC %md
# MAGIC Users active after midnight sleep less and show higher depression scores, indicating circadian disruption as a key digital health risk.

# COMMAND ----------

# DBTITLE 1,Late Night Usage Impact
display(spark.sql("""
SELECT 
    LateNight_Sleep_Risk,
    AVG(High_Mental_Health_Risk) AS Risk_Rate
FROM ecommerce.mental_health.silver_user_features
GROUP BY LateNight_Sleep_Risk
"""))


# COMMAND ----------

# MAGIC %md
# MAGIC Female users show slightly higher average anxiety and depression scores, with over 41% classified as high mental health risk. This suggests gender-specific vulnerability to digital stressors.

# COMMAND ----------

# DBTITLE 1,Gender vs Mental Health Risk
display(spark.sql("""
SELECT *
FROM ecommerce.mental_health.gold_gender_mental_health_summary
"""))

