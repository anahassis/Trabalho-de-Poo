import os
from tabuleiro import Tabuleiro

x = int(input("Quant. Vertical: "))
y = int(input("Quant. Horizontal: "))

tabuleiro = Tabuleiro(x,y)

while True:
    os.system('cls')
    print(tabuleiro)
    resposta = input("Qual casa (break = quitar): ")
    if resposta == "break" or resposta == "quitar":
        break
    tabuleiro.clicar(int(resposta[0]),int(resposta[1]))
print()
print("Easy peasy lemon squeezy")