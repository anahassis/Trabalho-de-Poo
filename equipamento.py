class Equipamento:
    def __init__(self,nome,patrimonio,dataAquisicao,status="Estoque"):
        self.__nome = nome
        self.__patrimonio = patrimonio 
        self.__dataAquisicao = dataAquisicao
        self.__status = status
        self.__manutencoes = []

    def __str__(self):
            return f"Nome: {self.__nome}, Patrimônio: {self.__patrimonio}, Data de Aquisição: {self.__dataAquisicao}, Status: {self.__status}, Quant. manutenções: {len(self.__manutencoes)}"

    def registrarManut(self,data_inicio,local_manut,duracao):
        self.__manutencoes.append([data_inicio,local_manut,duracao])  

    def mostrarManuts(self):
        texto = ""
        for manut in self.__manutencoes:
            texto += f"\n{manut[0]} - {manut[1]} - {manut[2]}"
        return texto

    def verificarStatus(self):
            return self.__status

    def atualizarStatus(self,status):
        match status:
            case 0:
                self.__status = "Uso"
            case 1:
                self.__status = "Estoque"
            case 2:
                self.__status = "Manutenção"

    def get_info(self,info):
        match info:
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