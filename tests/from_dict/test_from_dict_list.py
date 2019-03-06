"""
Asserts that list conversion works.
"""

from py_jobject import from_dict
from ..objects import Person, PersonCatalog

def test_from_dict_list():
    """
    Execute the test.
    """

    source = {
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

    result = from_dict(source, PersonCatalog)

    assert isinstance(result, PersonCatalog)
    assert isinstance(result.people, list)
    assert len(result.people) == 2

    assert isinstance(result.people[0], Person)
    assert result.people[0].name == 'Fernando Cicconeto'
    assert result.people[0].age == 29

    assert isinstance(result.people[1], Person)
    assert result.people[1].name == 'Paulo da Silva'
    assert result.people[1].age == 40
