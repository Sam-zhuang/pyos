""" Commands of pyos CPU. """
# arithmetic and logical commands
ADD = 0x01
SUB = 0x02
AND = 0x03
OR  = 0x04
NOT = 0x05
XOR = 0x06
LSH = 0x07
RSH = 0x08

# IO
IN  = 0x1A  # get from disk
OUT = 0x1B
GET = 0x1C  # get from memory
MOV = 0x1D

# control
STP = 0xFF
NOP = 0x00

# special constants
NUL = 0xEE

__all__ = vars()
del __all__["__name__"], __all__["__doc__"], __all__["__package__"], __all__["__loader__"], __all__["__spec__"]
