"""
`Decimal` definitions module.
"""

from decimal import Decimal

__all__ = [
    'DecimalDefinition'
]

class DecimalDefinition:
    """
    `Decimal` type definition.
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

        return Decimal(source)
