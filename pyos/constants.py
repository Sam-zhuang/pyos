""" Commands of pyos CPU. """
from types import FunctionType as _FunctionType
from functools import wraps as _wraps


class _Command:
    """ Decorator of CPU command. """
    def __init__(self, number):
        if not isinstance(number, _FunctionType):
            raise TypeError(f"func argument must be a function, not {type(number).__name__}")
        self.number = number

    def __call__(self, func):
        self.func = func

        @_wraps
        def wrapper(*args, **kwargs):
            func.is_command = True
            func.command_number = self.number
            v = func(args, kwargs)
            return v
        return wrapper

    def __repr__(self):
        return f'command {self.func.__name__}'


@_Command(0x00)
def _ADD(a, b):
    """ Command of add. """
    return a + b


@_Command(0x01)
def _SUB(a, b):
    return a - b


ADD = _ADD
SUB = _SUB
