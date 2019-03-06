"""
Module initialization.
"""

from .definitions import get_type_definition, set_type_definition
from .errors import UndefinedTypeError
from .from_func import from_dict
from .to_func import to_dict

__all__ = [
    'get_type_definition',
    'set_type_definition',
    'UndefinedTypeError',
    'from_dict',
    'to_dict'
]
