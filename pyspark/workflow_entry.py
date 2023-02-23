import argparse
import ast
from pipeline_workflow.default_workflow import DefaultWorkflow
from pipeline_utils.package import SparkParams 
from pyspark.sql import SparkSession

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--params", required=True, help="Spark input parameters")
args = parser.parse_args()

print('args ' + str(args))

def parse_command_line(args):
    return ast.literal_eval(args)


def spark_init(parser_name):
    
    ss = SparkSession \
        .builder \
        .appName(parser_name) \
        .getOrCreate()
    ss.sparkContext.setLogLevel("ERROR")
    return ss

params = parse_command_line(args.params)
print('runnung stuff ' + str(params))
params = SparkParams(params)
spark = spark_init(params.args['name'])

if __name__ == "__main__":
   
    print("Executing script via python")
    #spark.read.parquet('file:/data/wcd').show()
    dataflow = DefaultWorkflow(params, spark)
    #spark.sparkContext.getConf().getAll()
    dataflow.run()
else:
    print("Importing script")
