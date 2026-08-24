import datetime as date
class Pessoa:
    def __init__(self,nome,cpf,dataNasc,telefone):
        self.__nome = nome
        self.__cpf = cpf
        self.__dataNasc = dataNasc
        self.__telefone = telefone

    def __str__(self):
        return f"Nome: {self.__nome}, CPF: {self.__cpf}, Data de Nascimento: {self.__dataNasc}, Telefone: {self.__telefone}"

    def calcularIdade(self):
        pass

    def atualizarDados(self,tipo,dado):
        match tipo:
            case 'nome':
                self.__nome = dado
            case 'cpf':
                self.__cpf = dado
            case 'dataNasc':
                self.__dataNasc = dado
            case ' telefone':
                self.__telefone = dado

    def get_info(self,tipo):
        match tipo:
            case 'nome':
                return self.__nome
            case 'cpf':
                return self.__cpf
            case 'dataNasc':
                return self.__dataNasc
            case 'telefone':
                return self.__telefone