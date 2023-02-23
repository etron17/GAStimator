from pipeline_workflow.abstract_workflow import AbstractWorkflow
from pipeline_step.pipeline_step_loader import PipelineStepLoader
import pipeline_custom
import pkgutil


class DefaultWorkflow(AbstractWorkflow):
    def __init__(self, params, spark):
        super().__init__(params, spark)
        self.params = params
        self.spark = spark

    def run(self):
        print('VALIDATING******* ' + str(self.params.args))
        file_type = self.params.args['file_type']
        print('file type ' + str(file_type))
        steps = super().get_config(file_type)
        print('config ' + str(steps))
        # step 1 - read the file as dataframe
        df = None
        for node in steps:
            custom_steps = set(
                [modname for importer, modname, ispkg in pkgutil.iter_modules(pipeline_custom.__path__)])
            temp_cls, params = PipelineStepLoader.get_class(node, self.params, custom_steps=custom_steps)
            df = temp_cls.run(self.spark, params, df)
