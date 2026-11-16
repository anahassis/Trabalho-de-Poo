class Exercicio:
    def __init__(self, nome, series, repeticoes):
        self.__nome = nome
        self.__series = series
        self.__seriesrealizadas = 0
        self.__repeticoes = repeticoes
        self.__execrealizadas = 0

    def executar(self):
        self.__execrealizadas += 1
        if self.__execrealizadas == self.__repeticoes:
            self.__execrealizadas = 0
            self.__seriesrealizadas += 1
            if self.__seriesrealizadas == self.__series:
                self.__seriesrealizadas = 0
        self.exibirDetalhes()

    def exibirDetalhes(self):
        print(f"{self.__nome}: {self.__execrealizadas}/{self.__repeticoes}, Séries: {self.__seriesrealizadas}/{self.__series}")