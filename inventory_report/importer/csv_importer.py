import csv
from .importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file):
        if file.endswith(".csv"):
            with open(file) as arquivo:
                return list(csv.DictReader(arquivo))
        else:
            raise ValueError("Arquivo inválido")
