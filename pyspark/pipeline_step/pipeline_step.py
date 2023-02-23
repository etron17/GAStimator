import abc

class PipelineStep(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        print("constructor")

    @abc.abstractmethod
    def run(self, *args):
        pass
