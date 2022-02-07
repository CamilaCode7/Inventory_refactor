from .importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file):
        if file.endswith(".xml"):
            with open(file) as arquivo:
                xml_arquivo = xmltodict.parse(arquivo.read())
                return xml_arquivo["dataset"]["record"]
        else:
            raise ValueError("Arquivo inválido")
