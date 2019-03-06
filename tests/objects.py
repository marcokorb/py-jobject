"""
Objects to use in unit testing.
"""

from datetime import date, datetime, time
from decimal import Decimal
from typing import List

class Person:
    """
    Basic person object declaration.
    """

    name: str
    age: int

class PersonCatalog:
    """
    Object declaration containing lists.
    """

    people: List[Person]

class SeveralDataTypes:
    """
    Object declaration containing several data types.
    """

    date: date
    time: time
    datetime: datetime
    decimal: Decimal
    integer: int
    floating: float
    string: str

class UndefinedTypes:
    """
    Object declaration containing undefined types.
    """

    value: set
