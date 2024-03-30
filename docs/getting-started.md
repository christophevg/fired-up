# Getting Started

### Minimal Survival Command

```console
% pip install fired-up
```

### An example

With `Fired Up` it is possible to run a command like this:

```console
% python examples/hello.py generate a_reversed_list 1,a,2,b then dump as_json
[
  "b",
  2,
  "a",
  1
]
```

The code to achieve this would be something like this:

```python
import json

from fired_up import FiredUp, Group

class Generator(Group):
  def a_reversed_list(self, lst):
    return list(reversed(lst))

class Dumper(Group):
  def as_json(self):
    return json.dumps(self.paste(), indent=2)

FiredUp(generate=Generator, dump=Dumper)
```

`Fired Up` provides the following support for creating a even "nicer" natural-ish command language: 

* a `Group` base class allows for simply creating a functional class, that has access to a `clipboard` using the `copy` and `paste` methods. You will hardly ever require the `copy` method, since the returned values of your methods are automatically `copy`'d onto the default clipboard.
* a `FiredUp` top-level class to bring together the `Groups` and fire them up
* a `then` method on `Groups` allows to _exit_ the current `Group` scope and return to the top-level `FiredUp` class to access a different `Group`
