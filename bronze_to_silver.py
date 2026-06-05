#Bronze to Silver
from pyspark.sql.functions import to_date, col

df_silver = (
    df_bronze
    .withColumn("order_date", to_date(col("order_date")))
    .fillna({"unit_price": 0, "quantity": 0, "sales_amount": 0})
    .dropDuplicates(["order_id"])
    .withColumn("unit_price", col("unit_price").cast("int"))
    .withColumn("quantity", col("quantity").cast("int"))
    .withColumn("sales_amount", col("sales_amount").cast("int"))
    .withColumn("discount", col("sales_amount") * 0.05)
    .withColumn("discount",col("discount").cast("int"))

    )

df_silver.show()

df_silver.writeTo("glue_catalog.de_lakehousedb.orders_silver") \
    .using("iceberg") \
    .tableProperty("format-version", "2") \
    .createOrReplace()

print("Bronze to Silver Completed")