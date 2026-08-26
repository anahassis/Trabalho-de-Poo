class Academia:
    def __init__(self, nome, endereco, telefone, alunos=None, instrutores=None, equipamentos=None):
        self.__nome = nome
        self.__endereço = endereco
        self.__telefone = telefone
        self.__alunos = alunos if isinstance(alunos, list) else ([alunos] if alunos else [])
        self.__instrutores = instrutores if isinstance(instrutores, list) else ([instrutores] if instrutores else [])
        self.__equipamentos = equipamentos if isinstance(equipamentos, list) else ([equipamentos] if equipamentos else [])

    def __str__(self):
        return f"Nome: {self.__nome}, Endereço: {self.__endereço}, Telefone: {self.__telefone}, Qnt Alunos: {len(self.__alunos)}, Qnt. Instrutores: {len(self.__instrutores)}"

    def get_info(self,tipo):
        match tipo:
            case 'nome':
                return self.__nome
            case 'endereco':
                return self.__endereço
            case 'telefone':
                return self.__telefone
            case 'alunos':
                return self.__alunos
            case 'instrutores':
                return self.__instrutores
            case ' equipamentos':
                return self.__equipamentos

    def cadastrarAluno(self, aluno):
        self.__alunos.append(aluno)

    def cadastrarInst(self, instrutor):
        self.__instrutores.append(instrutor)

    def cadastrarEquip(self, equipamento):
        self.__equipamentos.append(equipamento)

    def listarEquip(self):
        all_equip = ""
        for equip in self.__equipamentos:
            all_equip += f"\n{equip}"
        return all_equip