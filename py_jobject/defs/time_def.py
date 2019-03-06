"""
`time` definitions module.
"""

from datetime import datetime

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

        return source.strftime('%H:%M:%S')

    @staticmethod
    def from_dict(source):
        """
        Converts from a dictionary data.
        """

        return datetime.strptime(source, '%H:%M:%S').time()
