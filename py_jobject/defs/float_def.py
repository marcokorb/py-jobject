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

        return float(source)

    @staticmethod
    def from_dict(source):
        """
        Converts from a dictionary data.
        """

        return float(source)
