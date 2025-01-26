import json
from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DoubleType, DateType
from pyspark.sql import SparkSession



def create_schema():
    """Creates a PySpark StructType based on the given JSON structure."""

    schema = StructType([
        StructField("bl_number", StringType(), True),
        StructField("bl_date", DateType(), True),
        StructField("trademark", StringType(), True),
        StructField("observation", StringType(), True),
        StructField("net_weight_identifier", StringType(), True),
        StructField("gross_weight_identifier", StringType(), True),
        StructField("container", ArrayType(StringType()), True),
        StructField("product", StringType(), True),
        StructField("transport_observation", StringType(), True),
        StructField("certification_status", StringType(), True),
        StructField("certification_type", StringType(), True),
        StructField("certification_history", ArrayType(
            StructType([
                StructField("action", StringType(), True),
                StructField("author", StringType(), True),
                StructField("date", DateType(), True)
            ])
        ), True),
        StructField("correction_letter", ArrayType(StringType()), True),
        StructField("origin", StringType(), True),
        StructField("certificate_number", StringType(), True),
        StructField("issue_date", DateType(), True),
        StructField("invoice_number", StringType(), True),
        StructField("transport", StringType(), True),
        StructField("loading_port", StringType(), True),
        StructField("country_of_origin", StringType(), True),
        StructField("destination_port", StringType(), True),
        StructField("country_of_destination", StringType(), True),
        StructField("net_weight", DoubleType(), True),
        StructField("gross_weight", DoubleType(), True),
        StructField("slaughter_date", ArrayType(StringType()), True),
        StructField("processing_package_date", ArrayType(StringType()), True),
        StructField("expiry_date", ArrayType(StringType()), True),
        StructField("description_quantity", StringType(), True),
        StructField("eco_hash", StringType(), True)
    ])

    return schema

def read_json_file(file_path):
    """Reads a JSON file and returns a PySpark DataFrame."""
    # Create a SparkSession
    #spark = SparkSession.builder.appName("My App").getOrCreate()

    schema = create_schema()

    with open(file_path, 'r') as f:
        data = json.load(f)

    # Create a list of dictionaries to represent the data
    data_list = [data]

    # Create a PySpark DataFrame from the list of dictionaries
    #df = spark.createDataFrame(data_list, schema)

    #return df
    return data_list

# Example usage
file_path = "sample.json"
data = read_json_file(file_path)
print(data)
#df = read_json_file(file_path)
#df.printSchema()