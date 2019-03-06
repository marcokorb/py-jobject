"""
Functions to convert from objects to dictionaries.
"""

from .definitions import get_type_definition

__all__ = [
    'to_dict'
]

def to_dict(source):
    """
    Converts from a `source` object to a dictionary.
    """

    if source is not None:
        return _to_dict_internal(source, type(source))

    return None

def _to_dict_internal(source, type_):
    if source is not None:
        definition = get_type_definition(type_)

        if definition is not None:
            return definition.to_dict(source)

        result = {}

        for name, value in source.__dict__.items():
            value_type = type_.__annotations__.get(name)

            if value_type is not None:
                value_result = _to_dict_internal(value, value_type)
            else:
                value_result = value

            result[name] = value_result

        return result

    return None
