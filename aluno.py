from pessoa import Pessoa
class Aluno(Pessoa):
    def __init__(self, nome, cpf, dataNasc,telefone,matricula,dataMatricula,plano,ficha,instrutor):
        super().__init__(nome, cpf, dataNasc,telefone)
        self.__matricula = matricula
        self.__dataMatricula = dataMatricula
        self.__plano = plano
        self.__instrutor = instrutor
        self.__ficha = ficha

    def __str__(self):
        return super().__str__() + f", Matricula: {self.__matricula}, Data de Matrícula: {self.__matricula}, Plano: {self.__plano}, Instrutor: {self.__instrutor}, Ficha: {self.__ficha}"

    def renovarPlano(self):
        pass

    def cancelarPlano(self):
        pass

    def consultarFicha(self):
        pass

    def pagarMensalidade(self):
        pass