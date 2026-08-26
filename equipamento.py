from datetime import date, datetime

class Equipamento:
    def __init__(self, nome, patrimonio, dataAquisicao, status="Estoque"):
        self.__nome = nome
        self.__patrimonio = patrimonio
        self.__dataAquisicao = datetime.strptime(dataAquisicao, "%d/%m/%Y").date() if isinstance(dataAquisicao, str) else dataAquisicao
        self.__status = status
        self.__manutencoes = []

    def __str__(self):
        data_str = self.__dataAquisicao.strftime("%d/%m/%Y") if isinstance(self.__dataAquisicao, date) else self.__dataAquisicao
        return f"Nome: {self.__nome}, Patrimônio: {self.__patrimonio}, Data de Aquisição: {data_str}, Status: {self.__status}, Quant. manutenções: {len(self.__manutencoes)}"

    def registrarManut(self, data_inicio, local_manut, duracao):
        d_inicio = datetime.strptime(data_inicio, "%d/%m/%Y").date() if isinstance(data_inicio, str) else data_inicio
        self.__manutencoes.append([d_inicio, local_manut, duracao])

    def mostrarManuts(self):
        texto = ""
        for manut in self.__manutencoes:
            d_str = manut[0].strftime("%d/%m/%Y") if isinstance(manut[0], date) else manut[0]
            texto += f"\n{d_str} - {manut[1]} - {manut[2]}"
        return texto

    def verificarStatus(self):
        return self.__status

    def atualizarStatus(self, status):
        match status:
            case 0:
                self.__status = "Uso"
            case 1:
                self.__status = "Estoque"
            case 2:
                self.__status = "Manutenção"

    def get_info(self, tipo):
        match tipo:
            case 0:
                return self.__nome
            case 1:
                return self.__patrimonio
            case 2:
                return self.__dataAquisicao
            case 3:
                return self.__status
            case 4:
                return self.__manutencoes

    def set_info(self, tipo, info):
        match tipo:
            case 0:
                self.__nome = info
            case 1:
                self.__patrimonio = info
            case 2:
                self.__dataAquisicao = datetime.strptime(info, "%d/%m/%Y").date() if isinstance(info, str) else info