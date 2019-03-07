"""
`Decimal` definitions module.
"""

from decimal import Decimal, InvalidOperation

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
            return Decimal(source)

        except InvalidOperation:
            return None
