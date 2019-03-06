"""
`date` definitions module.
"""

from datetime import datetime

__all__ = [
    'DateDefinition'
]

class DateDefinition:
    """
    `date` type definition.
    """

    @staticmethod
    def to_dict(source):
        """
        Converts to a dictionary data.
        """

        return source.strftime('%Y-%m-%d')

    @staticmethod
    def from_dict(source):
        """
        Converts from a dictionary data.
        """

        return datetime.strptime(source, '%Y-%m-%d').date()
