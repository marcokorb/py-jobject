"""
Asserts that to_dict accept date strings.
"""

from py_jobject import to_dict
from ..objects import SeveralDataTypes

def test_to_dict_accepts_date_string():
    """
    Execute the test.
    """

    obj = SeveralDataTypes()
    obj.date = '2019-03-06'
    obj.time = '15:36:21'
    obj.datetime = '2019-03-06 15:36:21'

    result = to_dict(obj)

    assert result == {
        'date': '2019-03-06',
        'time': '15:36:21',
        'datetime': '2019-03-06 15:36:21'
    }
