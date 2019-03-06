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

    return _from_dict_internal(source, type_)

def _from_dict_internal(source, type_):
    if source is not None:
        definition = get_type_definition(type_)

        if definition is not None:
            return definition.from_dict(source)

        result = type_()

        for name, value in source.items():
            value_type = type_.__annotations__.get(name)

            if value_type is not None:
                value_result = _from_dict_internal(value, value_type)
            else:
                value_result = value

            setattr(result, name, value_result)

        return result

    return None
