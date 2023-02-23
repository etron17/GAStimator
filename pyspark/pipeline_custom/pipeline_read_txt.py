from pipeline_step.pipeline_step import PipelineStep

class PipelineReadTxt(PipelineStep):
    def __init__(self):
        super().__init__()
        print('Read File')

    def run(self, spark, params, df):
        path = params.args['input_path']
        spark.read.option('header','true').csv(path).show()
        return spark.read.option('header','true').csv(path)
