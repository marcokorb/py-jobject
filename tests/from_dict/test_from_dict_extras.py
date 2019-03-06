"""
Asserts that the result contains additional attributes.
"""

from py_jobject import from_dict
from ..objects import Person

def test_from_dict_extras():
    """
    Execute the test.
    """

    source = {
        'name': 'Fernando Cicconeto',
        'age': 29,
        'city': 'Caxias do Sul'
    }

    result = from_dict(source, Person)

    assert isinstance(result, Person)
    assert result.name == 'Fernando Cicconeto'
    assert result.age == 29
    assert result.city == 'Caxias do Sul'
