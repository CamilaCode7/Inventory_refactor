import json
from .importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file):
        if file.endswith(".json"):
            with open(file) as arquivo:
                return json.load(arquivo)
        else:
            raise ValueError("Arquivo inválido")
