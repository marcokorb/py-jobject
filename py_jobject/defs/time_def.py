"""
`time` definitions module.
"""

from datetime import datetime
from ..util import datetime_to_dict

__all__ = [
    'TimeDefinition'
]

class TimeDefinition:
    """
    `time` type definition.
    """

    @staticmethod
    def to_dict(source):
        """
        Converts to a dictionary data.
        """

        return datetime_to_dict(source, '%H:%M:%S')

    @staticmethod
    def from_dict(source):
        """
        Converts from a dictionary data.
        """

        try:
            return datetime.strptime(source, '%H:%M:%S').time()

        except ValueError:
            return None
