"""
`float` definitions module.
"""

__all__ = [
    'FloatDefinition'
]

class FloatDefinition:
    """
    `float` type definition.
    """

    @staticmethod
    def to_dict(source):
        """
        Converts to a dictionary data.
        """

        try:
            return float(source)

        except ValueError:
            return None

    @staticmethod
    def from_dict(source):
        """
        Converts from a dictionary data.
        """

        try:
            return float(source)

        except ValueError:
            return None
