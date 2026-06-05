from pyspark.sql.functions import sum, countDistinct

daily_sales = (
    df_silver
    .groupBy("order_date")
    .agg(
        countDistinct("order_id").alias("total_orders"),
        sum("quantity").alias("total_quantity"),
        sum("sales_amount").alias("total_sales")
    )
    .orderBy("order_date")
).withColumn("total_orders", col("total_orders").cast("int")).withColumn("total_quantity", col("total_quantity").cast("int")).withColumn("total_sales", col("total_sales").cast("int"))



daily_sales.writeTo("glue_catalog.de_lakehousedb.daily_sales") \
    .using("iceberg") \
    .tableProperty("format-version", "2") \
    .createOrReplace()

print("Silver to Gold Completed")