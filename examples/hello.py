import json

from fired_up import FiredUp, Group

class Generator(Group):
  def a_reversed_list(self, lst):
    return list(reversed(lst))

class Dumper(Group):
  def as_json(self):
    return json.dumps(self.paste(), indent=2)

FiredUp(generate=Generator, dump=Dumper)
