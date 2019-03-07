"""
Type definitions controller module.
"""

from datetime import date, datetime, time
from decimal import Decimal
from typing import List

from .defs import (
    DateDefinition,
    DatetimeDefinition,
    DecimalDefinition,
    FloatDefinition,
    IntDefinition,
    ListDefinition,
    ObjectDefinition,
    StringDefinition,
    TimeDefinition
)
from .errors import UndefinedTypeError

__all__ = [
    'get_type_definition',
    'set_type_definition'
]

STATIC_TYPE_DEFINITIONS = {
    date: DateDefinition(),
    datetime: DatetimeDefinition(),
    Decimal: DecimalDefinition(),
    float: FloatDefinition(),
    int: IntDefinition(),
    str: StringDefinition(),
    time: TimeDefinition()
}

def get_type_definition(type_):
    """
    Gets a type definition.
    """

    definition = STATIC_TYPE_DEFINITIONS.get(type_)
    if definition is None:
        if type_.__name__ == List.__name__:
            return ListDefinition(type_.__args__[0])

        if hasattr(type_, '__annotations__'):
            return ObjectDefinition(type_)

        raise UndefinedTypeError(type_)

    return definition
