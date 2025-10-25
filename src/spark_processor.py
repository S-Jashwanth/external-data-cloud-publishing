# This module contains PySpark job wrappers for production usage.
from pyspark.sql import SparkSession

def get_spark(app_name='app'):
    spark = SparkSession.builder.appName(app_name).getOrCreate()
    return spark
