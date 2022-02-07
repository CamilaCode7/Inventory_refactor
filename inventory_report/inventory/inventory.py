from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import xmltodict
import json


class Inventory:
    @staticmethod
    def import_data(path, tipo):
        with open(path) as file:
            if path.endswith(".csv"):
                # Cria um dicionario e coloca o valor dentro do dicionario

                # status_reader = []
                # csv_read = csv.DictReader(file)
                # for row in csv_read:
                #     status_reader.append(row)

                # Forma alternativa e mais facil de fazer
                status_reader = list(csv.DictReader(file))

            if path.endswith(".json"):
                status_reader = json.load(file)
            if path.endswith(".xml"):
                # ler um dicionaro e acessa os elementos ["dataset"]["record"]
                # https://python-guide-pt-br.readthedocs.io/pt_BR/latest/scenarios/xml.html
                doc = xmltodict.parse(file.read())
                status_reader = doc["dataset"]["record"]
            if tipo == "simples":
                return SimpleReport.generate(status_reader)
            else:
                return CompleteReport.generate(status_reader)
