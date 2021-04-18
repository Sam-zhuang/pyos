""" Commands of pyos CPU. """
from functools import wraps as _wraps


class _Command:
    """ Decorator of CPU command. """
    def __init__(self, number):
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
        return f'command {self.number}: {self.func.__name__}'


@_Command(0x01)
def _ADD(a, b):
    """ Command of add. """
    return a + b


@_Command(0x02)
def _SUB(a, b):
    """ Command of subtract. """
    return a - b


@_Command(0x04)
def _LSH(a, b):
    """ Command of left shift. """
    return a << b


@_Command(0x08)
def _RSH(a, b):
    """ Command of right shift. """
    return a >> b


@_Command(0x10)
def _AND(a, b):
    """ Command of bitwise and. """
    return a & b


@_Command(0x20)
def _OR(a, b):
    """ Command of bitwise or. """
    return a | b


@_Command(0x40)
def _NOT(a):
    """ Command of bitwise not. """
    return ~a


@_Command(0x80)
def _NAND(a, b):
    return _NOT(_AND(a, b))


@_Command(0x100)
def _XOR(a, b):
    return not (a or b)


ADD = _ADD
SUB = _SUB
LSH = _LSH
RSH = _RSH
AND = _AND
OR = _OR
NOT = _NOT
NAND = _NAND
XOR = _XOR
