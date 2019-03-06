"""
Functions to convert from dictionaries to objects.
"""

from .definitions import get_type_definition

__all__ = [
    'from_dict'
]

def from_dict(source, type_):
    """
    Converts from a `source` dictionary to a object of class `type`.
    """

    definition = get_type_definition(type_)

    if source is not None:
        return definition.from_dict(source)

    return None
