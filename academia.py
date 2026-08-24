class Pessoa:
    def __init__(self,nome,cpf,dataNasc):
        self.nome = nome
        self.cpf = cpf
        self.dataNasc = dataNasc

    def renovarPlano(self):
        pass

    def cancelarPlano(self):
        pass

    def consultarFicha(self):
        pass

    def pagarMennsalidade(self):
        pass

class Instrutor(Pessoa):
    def __init__(self, nome, cpf, dataNasc,especialidade,cref):
        super().__init__(nome, cpf, dataNasc)
        self.especialidade = especialidade
        self.cref = cref

    def avaliarAluno(self,aluno):
        pass

    def criarFicha(self,aluno):
        pass

    def atualizarFicha(self,aluno):
        pass

    def consultarAgenda(self):
        pass
    
    

class Aluno(Pessoa):
    def __init__(self, nome, cpf, dataNasc,matricula,plano):
        super().__init__(nome, cpf, dataNasc)
        self.matricula = matricula
        self.plano = plano

    def renovarPlano(self):
        pass

    def cancelarPlano(self):
        pass

    def consultarFicha(self):
        pass

    def pagarMensalidade(self):
        pass
    

class Academia:
    def __init__(self,nome,endereco):
        self.nome = nome
        self.endereço = endereco

    def cadastrarAluno(self):
        pass

    def cadastrarInst(self):
        pass

    def listrarEquip(self):
        pass

class equipamento:
    def __init__(self,nome,patrimonio):
        self.nome = nome
        self.patrimonio = patrimonio 

    def verificarStatus(self):
        pass

    def registrarManut(self):
        pass

    def atualizarStatus(self):
        pass


class FichaDeTreino:
    def __init__(self,datacriacao,objetivo):
        self.datacriacao = datacriacao
        self.objetivo = datacriacao

    def addExercicio(self):
        pass

    def removerRexercicio(self):
        pass

    def calcularDuracao(self):
        pass

    def listarExercicios(self):
        pass


class Exercicio:
    def __init__(self,nome,series,repeticoes):
        self.nome = nome
        self.series = series
        self.repeticoes

    def executar(self):
        pass

    def ajustarCarga(self):
        pass

    def exibirDetalhes(self):
        pass

