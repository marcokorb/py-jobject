"""
Asserts that several type conversions work.
"""

from py_jobject import to_dict
from ..objects import SeveralDataTypes

def test_to_dict_error_proof():
    """
    Execute the test.
    """

    obj = SeveralDataTypes()
    obj.date = 'dgafh'
    obj.time = 'fadhaf'
    obj.datetime = 'dgad'
    obj.decimal = 'fhjsg'
    obj.integer = 'rhar'
    obj.floating = 'gjaobre'

    result = to_dict(obj)

    assert result == {
        'date': None,
        'time': None,
        'datetime': None,
        'decimal': None,
        'integer': None,
        'floating': None
    }
