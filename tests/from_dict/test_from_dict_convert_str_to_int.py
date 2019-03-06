"""
Asserts that converts a `str` to a `int`.
"""

from py_jobject import from_dict
from ..objects import Person

def test_from_dict_convert_str_to_int():
    """
    Execute the test.
    """

    source = {
        'name': 'Fernando Cicconeto',
        'age': '29'
    }

    result = from_dict(source, Person)

    assert isinstance(result, Person)
    assert result.name == 'Fernando Cicconeto'
    assert result.age == 29
