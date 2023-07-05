from fired_up import FiredUp, Group

class Left(Group):
  def __init__(self, write, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self._write = write

  def write(self):
    if self._write:
      self._globals["message"] = "left was here"

  def read(self):
    print("left>", self._globals["message"])

class Right(Group):
  def readwrite(self):
    print("right>", self._globals["message"])
    self._globals["message"] = "right was here too"

FiredUp(left=(Left, { "write" : True }), right=Right)
