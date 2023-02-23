from pyspark.sql import functions as f
from pipeline_step.pipeline_step import PipelineStep


class PipelineTransformTxt(PipelineStep):
    def __init__(self):
        super().__init__()
        print('transform data')

    def run(self, spark, params, df):
        df = df.withColumn('source', f.lit('wcd'))
        return df 
