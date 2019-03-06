"""
Asserts that list conversion works.
"""

from py_jobject import to_dict
from ..objects import Person, PersonCatalog

def test_to_dict_list():
    """
    Execute the test.
    """

    obj = PersonCatalog()
    obj.people = list()

    obj_0 = Person()
    obj_0.name = 'Fernando Cicconeto'
    obj_0.age = 29
    obj.people.append(obj_0)

    obj_1 = Person()
    obj_1.name = 'Paulo da Silva'
    obj_1.age = 40
    obj.people.append(obj_1)

    result = to_dict(obj)

    assert result == {
        'people': [
            {
                'name': 'Fernando Cicconeto',
                'age': 29
            },
            {
                'name': 'Paulo da Silva',
                'age': 40
            }
        ]
    }
