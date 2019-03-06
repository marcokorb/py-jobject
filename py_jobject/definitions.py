"""
Type definitions controller module.
"""

from datetime import date, datetime, time
from decimal import Decimal

from .defs import (
    DateDefinition,
    DatetimeDefinition,
    DecimalDefinition,
    FloatDefinition,
    IntDefinition,
    ObjectDefinition,
    StringDefinition,
    TimeDefinition
)
from .errors import UndefinedTypeError

__all__ = [
    'get_type_definition'
]

TYPE_DEFINITIONS = {
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

    definition = TYPE_DEFINITIONS.get(type_)
    if definition is None:
        if hasattr(type_, '__annotations__'):
            return ObjectDefinition(type_)

        raise UndefinedTypeError(type_)

    return definition
