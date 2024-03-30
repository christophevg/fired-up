# What's in The Box?

## Your Fired Up Command Line

`Fire` is a fun module that allows for providing a quick and beautiful command line interface on top of Python modules. `FiredUp` adds some baseclasses and conventions to make this experience even more fun, by enabling chaining multiple top-level commands/classes out of the box, using a shared clipboard.

### And _then_...

The [Fire Guide](https://google.github.io/python-fire/guide/#grouping-commands) has an example of grouping:

```python
import fire

class IngestionStage(object):
  def run(self):
    return 'Ingesting! Nom nom nom...'

class DigestionStage(object):
  def run(self, volume=1):
    return ' '.join(['Burp!'] * volume)

  def status(self):
    return 'Satiated.'

class Pipeline(object):
  def __init__(self):
    self.ingestion = IngestionStage()
    self.digestion = DigestionStage()

  def run(self):
    ingestion_output = self.ingestion.run()
    digestion_output = self.digestion.run()
    return [ingestion_output, digestion_output]

if __name__ == '__main__':
  fire.Fire(Pipeline)
```

Running this produces the following output

```console
% PYTHONPATH=. python examples/fire-group.py ingestion run
Ingesting! Nom nom nom...
% PYTHONPATH=. python examples/fire-group.py digestion run
Burp!
% PYTHONPATH=. python examples/fire-group.py digestion status
Satiated.
% PYTHONPATH=. python examples/fire-group.py run             
Ingesting! Nom nom nom...
Burp!
```

With `FiredUp` this grouping is even improved upon. 

First, given a few minor alterations, the same is still possible:

```python
from fired_up import FiredUp, Group

class IngestionStage(Group):
  def run(self):
    return 'Ingesting! Nom nom nom...'

class DigestionStage(Group):
  def run(self, volume=1):
    return ' '.join(['Burp!'] * volume)

  def status(self):
    return 'Satiated.'

class Pipeline(FiredUp):
  def run(self):
    ingestion_output = self.ingestion.run().paste()
    digestion_output = self.digestion.run().paste()
    return [ingestion_output, digestion_output]

if __name__ == "__main__":
  Pipeline(ingestion=IngestionStage, digestion=DigestionStage)
```

This runs with exactly the same results:

```console
% PYTHONPATH=. python examples/fired-up-group.py ingestion run
Ingesting! Nom nom nom...
% PYTHONPATH=. python examples/fired-up-group.py digestion run
Burp!
% PYTHONPATH=. python examples/fired-up-group.py digestion status
Satiated.
% PYTHONPATH=. python examples/fired-up-group.py run             
Ingesting! Nom nom nom...
Burp!
```

Now we can do one better and remove the `Pipeline` all together:

```python
from fired_up import FiredUp, Group

class IngestionStage(Group):
  def run(self):
    return 'Ingesting! Nom nom nom...'

class DigestionStage(Group):
  def run(self, volume=1):
    return ' '.join(['Burp!'] * volume)

  def status(self):
    return 'Satiated.'

if __name__ == "__main__":
  FiredUp(ingestion=IngestionStage, digestion=DigestionStage)
```

This runs exactly the same, except for the `Pipeline.run` command, which is now replaced with the sequencer `then` on the command line itself:

```console
% PYTHONPATH=. python examples/fired-up-group-minimal.py ingestion run
Ingesting! Nom nom nom...
% PYTHONPATH=. python examples/fired-up-group-minimal.py digestion run
Burp!
% PYTHONPATH=. python examples/fired-up-group-minimal.py digestion status
Satiated.
% PYTHONPATH=. python examples/fired-up-group-minimal.py --all ingestion run then digestion run
Ingesting! Nom nom nom...
Burp!
```

> Note the `--all` switch, which instructs `FiredUp` to return _all_ returned output as a list in stead of only the last returned value from the laste invoked method/command. Without it only "Burp!" would have been returned.
