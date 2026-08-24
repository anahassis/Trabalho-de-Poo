class Academia:
    def __init__(self,nome,endereco,telefone,horario,alunos,instrutores,equipamentos):
        self.__nome = nome
        self.__endereço = endereco
        self.__telefone = telefone
        self.__horario = horario
        self.__alunos = []
        self.__alunos.append(alunos)
        self.__instrutores = []
        self.__instrutores.append(instrutores)
        self.__equipamentos = []
        self.__equipamentos.append(equipamentos)

    def cadastrarAluno(self,aluno):
        self.__alunos.append(aluno)

    def cadastrarInst(self,instrutor):
        self.__instrutores.append(instrutor)

    def cadastrarEquip(self,equipamento):
        self.__equipamentos.append(equipamento)

    def listarEquip(self):
        all_equip = ""
        for equip in self.__equipamentos:
            all_equip += f"\n{equip}"  
        return all_equip

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