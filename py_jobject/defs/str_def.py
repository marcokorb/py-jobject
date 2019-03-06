"""
`str` definitions module.
"""

__all__ = [
    'StringDefinition'
]

class StringDefinition:
    """
    `str` type definition.
    """

    @staticmethod
    def to_dict(source):
        """
        Converts to a dictionary data.
        """

        return str(source)

    @staticmethod
    def from_dict(source):
        """
        Converts from a dictionary data.
        """

        return str(source)
