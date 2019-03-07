"""
Asserts that is ignoring non-existent attributes.
"""

from py_jobject import to_dict
from ..objects import Person

def test_to_dict_ignore_non_existent():
    """
    Execute the test.
    """

    obj = Person()
    obj.name = 'Fernando Cicconeto'

    result = to_dict(obj)

    assert result == {
        'name': 'Fernando Cicconeto'
    }
