from pessoa import Pessoa
class Instrutor(Pessoa):
    def __init__(self, nome, cpf, dataNasc,telefone,especialidade,cref,cargaHoraria,alunos):
        super().__init__(nome, cpf, dataNasc,telefone)
        self.__especialidade = especialidade
        self.__cref = cref
        self.__cargaHoraria = cargaHoraria
        self.__alunos = alunos

    def __str__(self):
        return super().__str__() + f", Especialidade: {self.__especialidade}, CREF: {self.__cref}, Carga Horária: {self.__cargaHoraria}, Quant. Alunos: {len(self.__alunos)}"

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
                case 'especialidade':
                    return self.__especialidade
                case 'cref':
                    return self.__cref
                case 'cargaHoraria':
                    return self.__cargaHoraria
                case 'alunos':
                    return self.__alunos
    
    def avaliarAluno(self,aluno):
        pass

    def criarFicha(self,aluno):
        pass

    def atualizarFicha(self,aluno):
        pass

    def consultarAgenda(self):
        pass