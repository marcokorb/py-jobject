# py-jobject

A package to easily convert between Python objects and JSON-compatible dictionaries, with built-in type conversion.

# Usage

- Declare a class with type-annotated attributes:

```python
class MyObject:

    foo: int
    bar: str
```

- Convert to a `dict` object:

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
