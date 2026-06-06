from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("SparkSQLDemo") \
    .getOrCreate()

data = [
    (1, "Ajay", 50000),
    (2, "Ravi", 60000),
    (3, "Kiran", 70000)
]

df = spark.createDataFrame(
    data,
    ["id", "name", "salary"]
)

df.show()

spark.stop()