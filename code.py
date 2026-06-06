from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create Spark Session
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("EmployeeDemo") \
    .getOrCreate()

# Sample Data
data = [
    (101, "Ajay", "IT", 50000),
    (102, "Ravi", "HR", 60000),
    (103, "Kiran", "IT", 70000),
    (104, "Sai", "Finance", 80000)
]

# Create DataFrame
df = spark.createDataFrame(
    data,
    ["emp_id", "emp_name", "department", "salary"]
)

print("Original Data:")
df.show()

print("Selected Columns:")
df.select("emp_name", "salary").show()

print("Salary > 60000:")
df.filter(col("salary") > 60000).show()

print("Annual Salary:")
df.select(
    "emp_name",
    (col("salary") * 12).alias("annual_salary")
).show()

spark.stop()