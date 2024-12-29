import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, pandas_udf
from sentence_transformers import SentenceTransformer
from pyspark.sql.types import ArrayType, FloatType


spark = SparkSession \
    .builder \
    .appName("Python PySpark Example") \
    .getOrCreate()


column_names = ["role", "description"]
data = [
    ("Data Analyst", "Analyzes data to help businesses make informed decisions."),
    ("Data Engineer", "Designs, builds, and maintains data pipelines and infrastructure."),
    ("Data Scientist", "Uses statistical techniques to analyze and interpret complex data."),
    ("DevOps Engineer", "Manages and automates deployment and operations of software systems."),
    ("Data Architect", "Designs and oversees the implementation of data architecture solutions.")
]
df = spark.createDataFrame(data, column_names)
df.show()




















