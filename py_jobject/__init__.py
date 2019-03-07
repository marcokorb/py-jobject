"""
Module initialization.
"""

from .errors import UndefinedTypeError
from .from_func import from_dict
from .to_func import to_dict

__all__ = [
    'UndefinedTypeError',
    'from_dict',
    'to_dict'
]
