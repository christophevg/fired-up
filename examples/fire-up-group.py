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
