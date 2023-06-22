from fired_up import FiredUp, Group

class IngestionStage(Group):
  def run(self):
    return 'Ingesting! Nom nom nom...'

class DigestionStage(Group):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self._volume = 1

  def volume(self, new_volume):
    self._volume = new_volume

  def run(self):
    return ' '.join(['Burp!'] * self._volume)

  def status(self):
    return 'Satiated.'

class Pipeline(FiredUp):
  def run(self):
    self.ingestion.run()
    ingestion_output = self.paste()
    self.digestion.run()
    digestion_output = self.paste()
    self.copy([ ingestion_output, digestion_output ])
    return self

if __name__ == "__main__":
  Pipeline(ingestion=IngestionStage, digestion=DigestionStage)
