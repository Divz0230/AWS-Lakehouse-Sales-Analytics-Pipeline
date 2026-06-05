# Raw to Bronze Layer
spark.conf.get("spark.sql.extensions", "NOT_SET")
spark.sql("SHOW DATABASES IN glue_catalog").show(truncate=False)
df_bronze = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv("s3://myde-prod-assets-875555915487-ap-south-1-an/raw/")
)

df_bronze.printSchema()

df_bronze.writeTo("glue_catalog.de_lakehousedb.orders_bronze") \
    .using("iceberg") \
    .tableProperty("format-version", "2") \
    .createOrReplace()

print("Raw to Bronze completed")