import random
class Tabuleiro:
    def __init__(self,x,y,qnt_bombas):
        self.qnt_bombas = qnt_bombas
        self.x = x
        self.y = y
        self.tabuleiro = [[None for _ in range(y)] for _ in range(x)]

    def pegar_vizinhos(self):
        pass

    def resetar(self):
        self.tabuleiro = [[None for _ in range(self.y)] for _ in range(self.x)]
        bombas_colocadas = 0
        while bombas_colocadas != self.qnt_bombas:
            self.tabuleiro[random.randint(0,self.x - 1)][random.randint(0,self.y - 1)]