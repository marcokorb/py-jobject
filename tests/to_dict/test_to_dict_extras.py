"""
Asserts that the result contains additional attributes.
"""

from py_jobject import to_dict
from ..objects import Person

def test_to_dict_extras():
    """
    Execute the test.
    """

    obj = Person()
    obj.name = 'Fernando Cicconeto'
    obj.age = 29
    obj.city = 'Caxias do Sul'

    result = to_dict(obj)

    assert result == {
        'name': 'Fernando Cicconeto',
        'age': 29,
        'city': 'Caxias do Sul'
    }
