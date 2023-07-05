from fired_up import FiredUp, __version__

def get_hello():
  return "hello"

def get_version():
  return __version__
  
FiredUp(hello=get_hello, version=get_version)
