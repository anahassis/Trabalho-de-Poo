from datetime import date, datetime

class Pessoa:
    def __init__(self, nome, cpf, dataNasc, telefone):
        self.__nome = nome
        self.__cpf = cpf
        self.__dataNasc = datetime.strptime(dataNasc, "%d/%m/%Y").date() if isinstance(dataNasc, str) else dataNasc
        self.__telefone = telefone

    def __str__(self):
        data_str = self.__dataNasc.strftime("%d/%m/%Y") if isinstance(self.__dataNasc, date) else self.__dataNasc
        return f"Nome: {self.__nome}, CPF: {self.__cpf}, Data de Nascimento: {data_str}, Telefone: {self.__telefone}"

    def calcularIdade(self):
        if isinstance(self.__dataNasc, date):
            hoje = date.today()
            return hoje.year - self.__dataNasc.year - ((hoje.month, hoje.day) < (self.__dataNasc.month, self.__dataNasc.day))
        return 0

    def atualizarDados(self, tipo, dado):
        match tipo:
            case 'nome':
                self.__nome = dado
            case 'cpf':
                self.__cpf = dado
            case 'dataNasc':
                self.__dataNasc = datetime.strptime(dado, "%d/%m/%Y").date() if isinstance(dado, str) else dado
            case 'telefone':
                self.__telefone = dado

    def get_info(self, tipo):
        match tipo:
            case 'nome':
                return self.__nome
            case 'cpf':
                return self.__cpf
            case 'dataNasc':
                return self.__dataNasc
            case 'telefone':
                return self.__telefone
        return None