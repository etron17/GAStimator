pipeline_step_loader.py
from functools import wraps
from importlib import import_module
from string import capwords
import pkgutil
from typing import Tuple
import pipeline_step 
from pipeline_step.pipeline_step import PipelineStep
import pipeline_step
from pipeline_step.pipeline_step import PipelineStep

common_steps = set([modname for importer, modname, ispkg in pkgutil.iter_modules(pipeline_step.__path__)])

def loaded(func):
    '''wrapper to check if module is common or custom
    Args:
        func -- function
    '''
    @wraps(func)
    def loading(*args, **kwargs):
        '''
        Expected *args:
            module_name
            params
        '''
        print(f'{func.__name__} was called')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        module_name, yaml_params = args
        prefix = 'pipeline_custom'
        full_mod_name = f'{prefix}.{module_name}'
        cls_name = capwords(module_name, sep='_').replace('_', '')
        return func(full_mod_name, cls_name, yaml_params)
    return loading


class PipelineStepLoader:
    @staticmethod
    @loaded
    def get_class(*args) -> Tuple[PipelineStep, type({})]:
        '''function to load pipeline step.
            wrapper will return expected args:
            [0] -- full_mod_name {str}
            [1] -- class name in module {str}
            [2] -- yaml params
        '''
        print(f'wrapper returned args: {args}')
        full_mod_name, cls_name, params = args
        mod_obj = import_module(full_mod_name)
        return getattr(mod_obj, cls_name)(), params
