"""

  conventions and supporting tools for using Fire in a more natural-ish
  language style

"""
__version__ = "0.0.6"

import sys
import functools

import fire

class Group():
  """
  
  baseclass for command groups
  
  """
  def __init__(self, _parent=None):
    self._parent = _parent

  @property
  def _globals(self):
    return self._shared["globals"]

  @property
  def _shared(self):
    if self._parent:
      return self._parent._shared
    return None

  def then(self):
    return self._shared["exit"]

  def copy(self, value, name="default"):
    self._shared["clipboard"][name] = value
    return self

  def paste(self, name="default"):
    return self._shared["clipboard"][name]

def keep(method):
  @functools.wraps(method)
  def wrapper(self, *args, **kwargs):
    result = method(self, *args, **kwargs)
    self.copy(result)
    if result:
      next(self._shared["clipboard"])
    return self
  return wrapper

class Clipboards():
  """
  
  simple multi-clipboard support
  
  """
  def __init__(self):
    self._boards = []
    next(self)

  def __next__(self):
    self._boards.append({"default": self["default"]})

  def __setitem__(self, key, value):
    self._boards[-1][key] = value

  def __getitem__(self, key):
    try:
      return self._boards[-1][key]
    except:
      pass
    return None

  def __str__(self):
    return str(self._boards)

class Menu(Group):
  """
  
  a menu is a set of groups or other menus
  
  """
  def __init__(self, **kwargs):
    super().__init__()
    for group, class_or_obj in kwargs.items():
      # unpack tuple(class_or_obj, arguments)
      if type(class_or_obj) is tuple:
        class_or_obj, args = class_or_obj
      else:
        args = {}
      # only handle classes, objects are used verbatim
      if isinstance(class_or_obj, type):
        # make sure all "public" methods return self to allow for chaining
        for attr in class_or_obj.__dict__:
          if callable(getattr(class_or_obj, attr)) and attr[0] != "_":
            setattr(class_or_obj, attr, keep(getattr(class_or_obj, attr)))
        self.__dict__[group] = class_or_obj(_parent=self, **args)
      elif isinstance(class_or_obj, Menu):
        # handle "sub"menu's, which are already objects and need merely a ref
        # to this parent, to allow for finding the top-level shared data
        self.__dict__[group] = class_or_obj
        class_or_obj._parent = self
      else:
        raise ValueError(f"Classes or other Menu'. Got '{type(class_or_obj)}'.")

class FiredUp(Menu):

  def __init__(self, name=None, command=None, all_results=False, **kwargs):
    self._actual_shared = {
      "clipboard" : Clipboards(),
      "globals"   : {},
      "exit"      : self
    }
    if "--all" in sys.argv:
      sys.argv.remove("--all")
      all_results = True

    if all_results:
      def paste_result(obj):
        return [board["default"] for board in obj._shared["clipboard"]._boards[:-1] ]
    else:
      def paste_result(obj):
        try:
          return obj.paste()
        except AttributeError:
          return obj
    
    super().__init__(**kwargs)
    try:
      fire.Fire(self, name=name, command=command, serialize=paste_result)
    except KeyboardInterrupt:
      pass

  @property
  def _shared(self):
    return self._actual_shared
