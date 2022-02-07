from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor():
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, tipo):
        recebe_data = self.importer.import_data(path)

        self.data.extend(recebe_data)

        if tipo == "simples":
            return SimpleReport.generate(recebe_data)

        if tipo == "completo":
            return CompleteReport.generate(recebe_data)

    def __iter__(self):
        return InventoryIterator(self.data)
