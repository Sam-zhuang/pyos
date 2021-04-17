""" Commands of pyos CPU. """
from types import FunctionType as _FunctionType


class _Command:
    """ Decorator of CPU command. """
    def __init__(self, func):
        if not isinstance(func, _FunctionType):
            raise TypeError(f"func argument must be a function, not {type(func).__name__}")
        self.func = func

    def __call__(self, *args, **kwargs):
        self.func.is_command = True
        v = self.func()
        return v


@_Command
def ADD(a, b):
    v1 = bin(int(str(a)))
