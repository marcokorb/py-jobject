# py-jobject

A package to easily convert between Python objects and JSON-compatible dictionaries, with built-in type conversion.

# Usage

- Declare a class with type-annotated attributes:

```python
class MyObject:

    foo: int
    bar: str
```

- Convert into a `dict` object:

```python
from py_jobject import to_dict

obj = MyObject()
obj.foo = 123
obj.bar = 'abc'

my_dict = to_dict(obj)

assert my_dict == {
   'foo': 123,
   'bar': 'abc'
}
```

- Convert from a `dict` object:

```python
from py_jobject import from_dict

my_dict = {
    'foo': 123,
    'bar': 'abc'
}

obj = from_dict(obj, MyObject)

assert obj.foo == 123
assert obj.bar == 'abc'
```

# Features

- Supports type conversion:

```python
from py_jobject import from_dict

my_dict = {
    'foo': '123',
}

obj = from_dict(obj, MyObject)

assert obj.foo == 123
```

- Extensibility:

```python
TZINFO_LOCAL = gettz('America/Sao_Paulo')

class BrazilianDatetimeDefinition:
    """
    Brazilian localized `datetime` definition.
    """

    @staticmethod
    def to_dict(source):
        """
        Converts to a dictionary data.
        """

        return source.astimezone(tz=TZINFO_LOCAL).strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def from_dict(source):
        """
        Converts from a dictionary data.
        """

        return datetime.strptime(source, '%Y-%m-%d %H:%M:%S').replace(tzinfo=TZINFO_LOCAL)

from py_jobject import set_type_definition, from_dict
set_type_definition(datetime, BrazilianDatetimeDefinition)

my_dict = {
    'datetime': '2019-03-06 15:36:21',
}

obj = from_dict(obj, MyObject)

assert obj.datetime == datetime(2019, 3, 6, 18, 36, 21, tzinfo=tzutc())
```
