"""
Functions to convert from objects to dictionaries.
"""

from .definitions import get_type_definition

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
        return definition.to_dict(source)

    return None
