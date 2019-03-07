"""
`date` definitions module.
"""

from datetime import datetime
from ..util import datetime_to_dict

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

        return datetime_to_dict(source, '%Y-%m-%d')

    @staticmethod
    def from_dict(source):
        """
        Converts from a dictionary data.
        """

        try:
            return datetime.strptime(source, '%Y-%m-%d').date()

        except ValueError:
            return None
