"""
Functions to convert from dictionaries to objects.
"""

from .definitions import get_type_definition
from typing import Union
from warnings import warn

__all__ = [
    'from_dict'
]

def from_dict(source, type_):
    """
    Converts from a `source` dictionary to a object of class `type`.
    """

    definition = get_type_definition(type_)

    if source is not None:
        if hasattr(type_, '__origin__') and type_.__origin__ is Union:
            for d in definition:
                try:
                    return d.from_dict(source)
                except Exception as e:
                    warn("Error calling from_dict for {content} to {cls}".format(
                        content=source,
                        cls=str(d.type_)
                    ))
        else:
            return definition.from_dict(source)

    return None
