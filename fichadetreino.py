from datetime import date, datetime
from exercicio import Exercicio

class FichaDeTreino:
    def __init__(self, datacriacao, objetivo):
        self.__datacriacao = datetime.strptime(datacriacao, "%d/%m/%Y").date() if isinstance(datacriacao, str) else datacriacao
        self.__objetivo = objetivo
        self.__exercicios = []

    def addExercicio(self, nome, series, repeticoes):
        self.__exercicios.append(Exercicio(nome, series, repeticoes))

    def removerRexercicio(self, index):
        if 0 <= index < len(self.__exercicios):
            self.__exercicios.pop(index)

    def calcularDuracao(self):
        return f"{len(self.__exercicios) * 15} min"

    def listarExercicios(self):
        for ex in self.__exercicios:
            ex.exibirDetalhes()