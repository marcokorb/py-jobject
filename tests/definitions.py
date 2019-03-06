"""
Brazilian localized `datetime` definitions module.
"""

from datetime import datetime
from dateutil.tz import gettz

TZINFO_LOCAL = gettz('America/Sao_Paulo')

class BrazilianDatetimeDefinition:
    """
    Brazilian localized `datetime` definition.
    """

    @staticmethod
    def to_dict(source):
        """
        Converts to a dictionary data.
        """

        return source.astimezone(tz=TZINFO_LOCAL).strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def from_dict(source):
        """
        Converts from a dictionary data.
        """

        return datetime.strptime(source, '%Y-%m-%d %H:%M:%S').replace(tzinfo=TZINFO_LOCAL)
