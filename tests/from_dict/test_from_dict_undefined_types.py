"""
Asserts that an exception is thrown when a type is not defined.
"""

from pytest import raises
from py_jobject import from_dict, UndefinedTypeError
from ..objects import UndefinedTypes

def test_from_dict_undefined_types():
    """
    Execute the test.
    """

    source = {
        'value': [1, 2, 3]
    }

    with raises(UndefinedTypeError, match="Type 'set' is not defined."):
        from_dict(source, UndefinedTypes)
