class Pessoa:
    def __init__(self,nome,cpf,dataNasc):
        self.nome = nome
        self.cpf = cpf
        self.dataNasc = dataNasc

class Instrutor(Pessoa):
    def __init__(self, nome, cpf, dataNasc,especialidade,cref):
        super().__init__(nome, cpf, dataNasc)
        self.especialidade = especialidade
        self.cref = cref

class Aluno(Pessoa):
    def __init__(self, nome, cpf, dataNasc,matricula,plano):
        super().__init__(nome, cpf, dataNasc)
        self.matricula = matricula
        self.plano = plano

class Academia:
    def __init__(self,nome,endereco):
        self.nome = nome
        self.endereço = endereco

class equipamento:
    def __init__(self,nome,patrimonio):
        self.nome = nome
        self.patrimonio = patrimonio 


class FichaDeTreino:
    def __init__(self,datacriacao,objetivo):
        self.datacriacao = datacriacao
        self.objetivo = datacriacao


class Exercicio:
    def __init__(self,nome,series,repeticoes):
        self.nome = nome
        self.series = series
        self.repeticoes

