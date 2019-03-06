"""
Asserts that several type conversions work.
"""

from datetime import date, datetime, time
from decimal import Decimal
from py_jobject import to_dict
from ..objects import SeveralDataTypes

def test_to_dict_several_types():
    """
    Execute the test.
    """

    obj = SeveralDataTypes()
    obj.date = date(2019, 3, 6)
    obj.time = time(15, 36, 21)
    obj.datetime = datetime(2019, 3, 6, 15, 36, 21)
    obj.decimal = Decimal('21.0')
    obj.integer = 12
    obj.floating = 13.5
    obj.string = 'qwerty'

    result = to_dict(obj)

    assert result == {
        'date': '2019-03-06',
        'time': '15:36:21',
        'datetime': '2019-03-06 15:36:21',
        'decimal': 21.0,
        'integer': 12,
        'floating': 13.5,
        'string': 'qwerty'
    }
