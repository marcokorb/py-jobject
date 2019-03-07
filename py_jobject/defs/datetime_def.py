"""
`datetime` definitions module.
"""

from datetime import datetime
from ..util import datetime_to_dict

__all__ = [
    'DatetimeDefinition'
]

class DatetimeDefinition:
    """
    `datetime` type definition.
    """

    @staticmethod
    def to_dict(source):
        """
        Converts to a dictionary data.
        """

        return datetime_to_dict(source, '%Y-%m-%d %H:%M:%S')

    @staticmethod
    def from_dict(source):
        """
        Converts from a dictionary data.
        """

        try:
            return datetime.strptime(source, '%Y-%m-%d %H:%M:%S')

        except ValueError:
            return None
