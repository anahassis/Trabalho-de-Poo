from datetime import date, datetime
from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, cpf, dataNasc, telefone, matricula, dataMatricula, plano="Básico", ficha="--", instrutor="--"):
        super().__init__(nome, cpf, dataNasc, telefone)
        self.__matricula = matricula
        self.__dataMatricula = datetime.strptime(dataMatricula, "%d/%m/%Y").date() if isinstance(dataMatricula, str) else dataMatricula
        self.__plano = plano
        self.__instrutor = instrutor
        self.__ficha = ficha
        self.__status = "Ativado"
        self.__nota = "--"

    def __str__(self):
        data_str = self.__dataMatricula.strftime("%d/%m/%Y") if isinstance(self.__dataMatricula, date) else self.__dataMatricula
        return super().__str__() + f", Matricula: {self.__matricula}, Data de Matrícula: {data_str}, Plano: {self.__plano}, Instrutor: {self.__instrutor}, Ficha: {self.__ficha}"

    def get_info(self, tipo):
        res = super().get_info(tipo)
        if res is not None:
            return res
        match tipo:
            case 'matricula':
                return self.__matricula
            case 'dataMatricula':
                return self.__dataMatricula
            case 'plano':
                return self.__plano
            case 'instrutor':
                return self.__instrutor
            case 'ficha':
                return self.__ficha
            case 'nota':
                return self.__nota
            case 'status':
                return self.__status

    def set_info(self, tipo, info):
        match tipo:
            case 'nome' | 'cpf' | 'dataNasc' | 'telefone':
                super().atualizarDados(tipo, info)
            case 'matricula':
                self.__matricula = info
            case 'dataMatricula':
                self.__dataMatricula = datetime.strptime(info, "%d/%m/%Y").date() if isinstance(info, str) else info
            case 'plano':
                self.__plano = info
            case 'instrutor':
                self.__instrutor = info
            case 'ficha':
                self.__ficha = info
            case 'nota':
                self.__nota = info
            case 'status':
                self.__status = info

    def alterarPlano(self, tipo):
        match tipo:
            case 0:
                self.__plano = "Básico"
            case 1:
                self.__plano = "Médio"
            case 2:
                self.__plano = "Avançado"

    def cancelarPlano(self):
        self.__status = "Desativado"

    def ativarPlano(self):
        self.__status = "Ativado"

    def consultarFicha(self):
        return self.__ficha