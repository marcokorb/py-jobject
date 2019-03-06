"""
Object definitions module.
"""

import py_jobject

__all__ = [
    'ObjectDefinition'
]

class ObjectDefinition:
    """
    Object type definition.
    """

    def __init__(self, type_):
        self.type_ = type_

    def to_dict(self, source):
        """
        Converts to a dictionary data.
        """

        result = {}

        for name, value in source.__dict__.items():
            value_type = self.type_.__annotations__.get(name)

            if value_type is not None:
                value_result = py_jobject.to_dict(value, value_type)
            else:
                value_result = value

            result[name] = value_result

        return result

    def from_dict(self, source):
        """
        Converts from a dictionary data.
        """

        result = self.type_()

        for name, value in source.items():
            value_type = self.type_.__annotations__.get(name)

            if value_type is not None:
                value_result = py_jobject.from_dict(value, value_type)
            else:
                value_result = value

            setattr(result, name, value_result)

        return result
