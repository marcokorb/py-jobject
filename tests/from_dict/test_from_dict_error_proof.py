"""
Asserts that exception handling works.
"""

from py_jobject import from_dict
from ..objects import SeveralDataTypes

def test_from_dict_error_proof():
    """
    Execute the test.
    """

    source = {
        'date': '0000-00-00',
        'time': 'aaa',
        'datetime': '0000-00-00 00:00:00',
        'decimal': 'b',
        'integer': '4j',
        'floating': 'fhasfh'
    }

    result = from_dict(source, SeveralDataTypes)

    assert isinstance(result, SeveralDataTypes)
    assert result.date is None
    assert result.time is None
    assert result.datetime is None
    assert result.decimal is None
    assert result.integer is None
    assert result.floating is None
