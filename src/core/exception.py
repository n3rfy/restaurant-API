from .exc_class import ExceptionAll
from ormar.exceptions import NoMatch
from .exc_class import ExceptionAll

import functools

def error(fn):
    
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except NoMatch:
            raise ExceptionAll(
                status_code=404,
                content = {'code':0,'message':'food id not found!'}
            )
    return inner
