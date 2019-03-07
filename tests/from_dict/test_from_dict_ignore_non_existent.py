"""
Asserts that is ignoring non-existent attributes.
"""

from py_jobject import from_dict
from ..objects import Person

def test_from_dict_non_existent():
    """
    Execute the test.
    """

    source = {
        'name': 'Fernando Cicconeto'
    }

    result = from_dict(source, Person)

    assert isinstance(result, Person)
    assert result.name == 'Fernando Cicconeto'
    assert not hasattr(result, 'age')
