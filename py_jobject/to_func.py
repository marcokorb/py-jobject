"""
Functions to convert from objects to dictionaries.
"""

from .definitions import get_type_definition
from warnings import warn
from typing import Union

__all__ = [
    'to_dict'
]


def to_dict(source, type_=None):
    """
    Converts from a `source` object to a dictionary.
    """

    if type_ is None:
        type_ = type(source)

    definition = get_type_definition(type_)

    if source is not None:
        if hasattr(type_, '__origin__') and type_.__origin__ is Union:
            for d in definition:
                try:
                    return definition.to_dict(source)
                except Exception as e:
                    warn("Error calling to_dict from {content} to dict".format(
                        content=source,
                        cls=str(d.type_)
                    ))
        else:
            return definition.to_dict(source)

    return None
