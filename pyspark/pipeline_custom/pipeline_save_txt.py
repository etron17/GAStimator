from pyspark.sql import functions as f
from pipeline_step.pipeline_step import PipelineStep


class PipelineSaveTxt(PipelineStep):
    def __init__(self):
        super().__init__()
        print('save data')

    def run(self, spark, params, df):
        output_path = params.args['output_path']
        partition_column = params.args['partition_column']
        df.write.option('header','true').partitionBy(partition_column).mode('append').parquet(output_path)
        return df 
