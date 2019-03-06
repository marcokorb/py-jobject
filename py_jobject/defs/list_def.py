"""
`List` definitions module.
"""

import py_jobject

__all__ = [
    'ListDefinition'
]

class ListDefinition:
    """
    `List` type definition.
    """

    def __init__(self, type_):
        self.type_ = type_

    def to_dict(self, source):
        """
        Converts to a dictionary data.
        """

        result = list()

        for item in source:
            result.append(py_jobject.to_dict(item, self.type_))

        return result

    def from_dict(self, source):
        """
        Converts from a dictionary data.
        """

        result = list()

        for item in source:
            result.append(py_jobject.from_dict(item, self.type_))

        return result
