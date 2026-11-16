from pessoa import Pessoa

class Instrutor(Pessoa):
    def __init__(self, nome, cpf, dataNasc, telefone, especialidade, cref, cargaHoraria, alunos=None):
        super().__init__(nome, cpf, dataNasc, telefone)
        self.__especialidade = especialidade
        self.__cref = cref
        self.__cargaHoraria = cargaHoraria
        self.__alunos = alunos if alunos is not None else []

    def __str__(self):
        return super().__str__() + f", Especialidade: {self.__especialidade}, CREF: {self.__cref}, Carga Horária: {self.__cargaHoraria}, Quant. Alunos: {len(self.__alunos)}"

    def get_info(self, tipo):
        res = super().get_info(tipo)
        if res is not None:
            return res
        match tipo:
            case 'especialidade':
                return self.__especialidade
            case 'cref':
                return self.__cref
            case 'cargaHoraria':
                return self.__cargaHoraria
            case 'alunos':
                return self.__alunos

    def set_info(self, tipo, info):
        match tipo:
            case 'nome' | 'cpf' | 'dataNasc' | 'telefone':
                super().atualizarDados(tipo, info)
            case 'especialidade':
                self.__especialidade = info
            case 'cref':
                self.__cref = info
            case 'cargaHoraria':
                self.__cargaHoraria = info
            case 'alunos':
                self.__alunos = info

    def avaliarAluno(self, aluno, nota):
        aluno.set_info('nota', nota)

    def atualizarFicha(self, aluno, ficha):
        aluno.set_info('ficha', ficha)