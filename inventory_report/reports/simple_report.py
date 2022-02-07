from datetime import datetime


class SimpleReport:
    EMPRESA = {}

    @classmethod
    def generate(cls, list):
        empresa = {}
        data_val = []
        data_de_fab = list[0]["data_de_fabricacao"]
        today = datetime.strftime(datetime.now(), "%Y-%m-%d")

        for index in list:
            if data_de_fab > index["data_de_fabricacao"]:
                data_de_fab = index["data_de_fabricacao"]
            if index["data_de_validade"] > today:
                data_val.append(index["data_de_validade"])
            if index["nome_da_empresa"] not in empresa.keys():
                empresa[index["nome_da_empresa"]] = 1
                # print(empresa)
            else:
                empresa[index["nome_da_empresa"]] += 1
            cls.EMPRESA = empresa
        return (
            f"Data de fabricação mais antiga: {data_de_fab}\n"
            f"Data de validade mais próxima: {min(data_val)}\n"
            "Empresa com maior quantidade de produtos estocados: "
            f"{max(empresa)}\n"
        )
