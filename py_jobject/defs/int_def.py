"""
`int` definitions module.
"""

__all__ = [
    'IntDefinition'
]

class IntDefinition:
    """
    `int` type definition.
    """

    @staticmethod
    def to_dict(source):
        """
        Converts to a dictionary data.
        """

        return int(source)

    @staticmethod
    def from_dict(source):
        """
        Converts from a dictionary data.
        """

        return int(source)
