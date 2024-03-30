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
