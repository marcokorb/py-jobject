"""
Utility functions module.
"""

from datetime import datetime

def datetime_to_dict(source, format_):
    """
    Converts a date-like object (`date`, `time`, `datetime`, ...) to a dictionary value.
    """

    if source is not None and hasattr(source, 'strftime'):
        return source.strftime(format_)

    try:
        date = datetime.strptime(source, format_)

    except ValueError:
        date = None

    if date is not None:
        return date.strftime(format_)

    return None
