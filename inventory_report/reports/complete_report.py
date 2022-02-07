from .simple_report import SimpleReport

# https://www.geeksforgeeks.org/class-method-vs-static-method-python/#:~:text=A%20class%20method%20takes%20cls,nothing%20about%20the%20class%20state.


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list):
        valor_empresa = ""
        simple_report = SimpleReport.generate(list)
        empresas = cls.EMPRESA
        for chave, value in empresas.items():
            valor_empresa += f"- {chave}: {value}\n"

        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa: \n"
            f"{valor_empresa}"
        )
