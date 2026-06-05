# AWS Lakehouse Sales Analytics Pipeline

## Overview

This project demonstrates an end-to-end AWS Lakehouse implementation using AWS Glue, Amazon S3, Apache Iceberg, and PySpark. The pipeline follows the Medallion Architecture (Bronze, Silver, Gold) to ingest, clean, transform, and aggregate sales data for analytics and reporting.

## Architecture

S3 Raw Data
↓
AWS Glue ETL (PySpark)
↓
Bronze Layer (Apache Iceberg)
↓
Silver Layer (Apache Iceberg)
↓
Gold Layer (Daily Sales Aggregation)
↓
Athena / BI Reporting

## Technologies Used

* AWS Glue 5.0
* Amazon S3
* Apache Iceberg
* PySpark
* AWS Glue Data Catalog
* Amazon Athena
* GitHub

## Project Structure

```text
aws-lakehouse-sales-analytics/
│
├── sales_lakehouse_pipeline.py
├── README.md
├── architecture.png
├── screenshots/
│   ├── bronze_table.png
│   ├── silver_table.png
│   ├── gold_table.png
│   └── glue_job.png
│
└── sample_data/
    └── orders.csv
```

## Data Pipeline Flow

### Raw Layer

Sales data is ingested from CSV files stored in Amazon S3.

### Bronze Layer

Raw data is loaded into an Apache Iceberg table without business transformations.

**Table:**

* orders_bronze

### Silver Layer

Data quality and transformation steps performed:

* Date conversion
* Null value handling
* Duplicate removal
* Data type casting
* Discount calculation

**Table:**

* orders_silver

### Gold Layer

Business-ready aggregated data is created for reporting and analytics.

**Table:**

* daily_sales

Metrics generated:

* Total Orders
* Total Quantity Sold
* Total Sales Amount

## Sample Gold Layer Output

| order_date | total_orders | total_quantity | total_sales |
| ---------- | ------------ | -------------- | ----------- |
| 2025-01-01 | 1            | 2              | 8464        |
| 2025-01-02 | 1            | 3              | 11853       |
| 2025-01-03 | 1            | 1              | 3540        |

## Iceberg Features Demonstrated

* Table Versioning
* Snapshot Management
* ACID Transactions
* Schema Evolution Support
* Metadata Tracking

## Scheduling

The AWS Glue Job is configured for scheduled execution using AWS Glue Scheduler.

Pipeline execution:

```text
Raw CSV
 → Bronze Iceberg
 → Silver Iceberg
 → Gold Aggregation
```

## Key Learnings

* Building Data Lakehouse architectures on AWS
* Working with Apache Iceberg tables
* Implementing Medallion Architecture
* Developing ETL pipelines using PySpark
* Managing data using AWS Glue Data Catalog
* Querying Iceberg tables through Athena

## Future Enhancements

* City-wise Sales Aggregation
* Category-wise Sales Analysis
* Monthly Sales Trends
* Customer Analytics
* Power BI / Tableau Dashboard Integration

## Author

Divya Umrekar

Data Engineer | PySpark | AWS Glue | Apache Iceberg | SQL

