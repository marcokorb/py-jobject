"""
Asserts that several type conversions work.
"""

from datetime import date, datetime, time
from decimal import Decimal
from py_jobject import from_dict
from ..objects import SeveralDataTypes

def test_from_dict_several_types():
    """
    Execute the test.
    """

    source = {
        'date': '2019-03-06',
        'time': '15:36:21',
        'datetime': '2019-03-06 15:36:21',
        'decimal': '21.0',
        'integer': '12',
        'floating': '13.5',
        'string': 'qwerty'
    }

    result = from_dict(source, SeveralDataTypes)

    assert isinstance(result, SeveralDataTypes)
    assert result.date == date(2019, 3, 6)
    assert result.time == time(15, 36, 21)
    assert result.datetime == datetime(2019, 3, 6, 15, 36, 21)
    assert result.decimal == Decimal('21.0')
    assert result.integer == 12
    assert result.floating == 13.5
    assert result.string == 'qwerty'
