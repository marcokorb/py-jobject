"""
Type definitions controller module.
"""

from .defs import IntDefinition, StringDefinition

__all__ = [
    'get_type_definition'
]

TYPE_DEFINITIONS = {
    int: IntDefinition(),
    str: StringDefinition()
}

def get_type_definition(type_):
    """
    Gets a type definition.
    """

    return TYPE_DEFINITIONS.get(type_)
