"""
Asserts that an exception is thrown when a type is not defined.
"""

from pytest import raises
from py_jobject import to_dict, UndefinedTypeError
from ..objects import UndefinedTypes

def test_to_dict_undefined_types():
    """
    Execute the test.
    """

    obj = UndefinedTypes()
    obj.value = [1, 2, 3]

    with raises(UndefinedTypeError, match="Type 'set' is not defined."):
        to_dict(obj)
