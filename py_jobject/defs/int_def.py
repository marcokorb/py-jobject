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

        try:
            return int(source)

        except ValueError:
            return None

    @staticmethod
    def from_dict(source):
        """
        Converts from a dictionary data.
        """

        try:
            return int(source)

        except ValueError:
            return None
