from academia import Academia
from aluno import Aluno
from instrutor import Instrutor
from equipamento import Equipamento
from fichadetreino import FichaDeTreino


def menu_principal():
    print("\n" + "=" * 35)
    print("SISTEMA DE GESTÃO DA ACADEMIA")
    print("1. Atendente (Gestão da Academia)")
    print("2. Instrutor")
    print("3. Aluno")
    print("0. Sair")
    print("=" * 35)


def menu_atendente():
    print("\n--- MENU ATENDENTE ---")
    print("1. Cadastrar Aluno")
    print("2. Cadastrar Instrutor")
    print("3. Cadastrar Equipamento")
    print("4. Listar Equipamentos")
    print("0. Voltar ao Menu Principal")


def menu_instrutor():
    print("\n--- MENU INSTRUTOR ---")
    print("1. Ver Meus Dados")
    print("2. Avaliar Aluno")
    print("3. Criar / Atualizar Ficha de Treino do Aluno")
    print("0. Voltar ao Menu Principal")


def menu_aluno():
    print("\n--- MENU ALUNO ---")
    print("1. Ver Meus Dados e Status")
    print("2. Ver Minha Idade")
    print("3. Consultar Ficha de Treino")
    print("4. Alterar Plano")
    print("5. Ativar Plano")
    print("6. Cancelar Plano")
    print("0. Voltar ao Menu Principal")


print("CONFIGURAÇÃO INICIAL DA ACADEMIA")
nome_ac = input("Nome da Academia: ")
end_ac = input("Endereço: ")
tel_ac = input("Telefone: ")
hor_ac = input("Horário de Funcionamento: ")

academia = Academia(nome_ac, end_ac, tel_ac, hor_ac)

alunos = []
instrutores = []

while True:
    menu_principal()
    opcao = input("Escolha o perfil de acesso: ")

    if opcao == "1":
        while True:
            menu_atendente()
            op_at = input("Escolha uma opção: ")

            if op_at == "1":
                print("\n[ Cadastro de Aluno ]")
                nome = input("Nome: ")
                cpf = input("CPF: ")
                data_nasc = input("Data de Nascimento (DD/MM/AAAA): ")
                telefone = input("Telefone: ")
                matricula = input("Matrícula: ")
                data_mat = input("Data da Matrícula (DD/MM/AAAA): ")
                plano = input("Plano (Básico/Médio/Avançado): ") or "Básico"

                novo_aluno = Aluno(
                    nome, cpf, data_nasc, telefone, matricula, data_mat, plano
                )
                academia.cadastrarAluno(novo_aluno)
                alunos.append(novo_aluno)
                print(f"Aluno '{nome}' cadastrado com sucesso!")

            elif op_at == "2":
                print("\n[ Cadastro de Instrutor ]")
                nome = input("Nome: ")
                cpf = input("CPF: ")
                data_nasc = input("Data de Nascimento (DD/MM/AAAA): ")
                telefone = input("Telefone: ")
                especialidade = input("Especialidade: ")
                cref = input("CREF: ")
                carga_horaria = input("Carga Horária: ")

                novo_instrutor = Instrutor(
                    nome,
                    cpf,
                    data_nasc,
                    telefone,
                    especialidade,
                    cref,
                    carga_horaria,
                )
                academia.cadastrarInst(novo_instrutor)
                instrutores.append(novo_instrutor)
                print(f"Instrutor '{nome}' cadastrado com sucesso!")

            elif op_at == "3":
                print("\n[ Cadastro de Equipamento ]")
                nome = input("Nome do Equipamento: ")
                patrimonio = input("Patrimônio: ")
                data_acq = input("Data de Aquisição (DD/MM/AAAA): ")

                novo_equip = Equipamento(nome, patrimonio, data_acq)
                academia.cadastrarEquip(novo_equip)
                print(f"Equipamento '{nome}' cadastrado com sucesso!")

            elif op_at == "4":
                print("\n[ Lista de Equipamentos ]")
                print(academia.listarEquip())

            elif op_at == "0":
                break
            else:
                print("Opção inválida!")

    elif opcao == "2":
        if not instrutores:
            print(
                "\nNenhum instrutor cadastrado. Solicite ao atendente o cadastro prévio."
            )
            continue

        print("\n--- SELECIONE O INSTRUTOR ---")
        for idx, inst in enumerate(instrutores):
            print(
                f"{idx + 1}. {inst.get_info('nome')} (CREF: {inst.get_info('cref')})"
            )

        try:
            escolha = int(input("Escolha seu perfil: ")) - 1
            if escolha < 0 or escolha >= len(instrutores):
                print("Instrutor não encontrado!")
                continue
            instrutor_atual = instrutores[escolha]
        except ValueError:
            print("Entrada inválida!")
            continue

        while True:
            menu_instrutor()
            op_inst = input("Escolha uma opção: ")

            if op_inst == "1":
                print(f"\n{instrutor_atual}")

            elif op_inst == "2":
                if not alunos:
                    print("Nenhum aluno cadastrado para avaliar.")
                    continue
                print("\n--- SELECIONE O ALUNO ---")
                for idx, al in enumerate(alunos):
                    print(
                        f"{idx + 1}. {al.get_info('nome')} (Matrícula: {al.get_info('matricula')})"
                    )

                try:
                    idx_al = int(input("Escolha o aluno: ")) - 1
                    if 0 <= idx_al < len(alunos):
                        nota = input("Digite a nota/avaliação do aluno: ")
                        instrutor_atual.avaliarAluno(alunos[idx_al], nota)
                        print("Avaliação registrada com sucesso!")
                    else:
                        print("Aluno inválido!")
                except ValueError:
                    print("Entrada inválida!")

            elif op_inst == "3":
                if not alunos:
                    print("Nenhum aluno cadastrado.")
                    continue
                print("\n--- CRIAR FICHA DE TREINO ---")
                for idx, al in enumerate(alunos):
                    print(f"{idx + 1}. {al.get_info('nome')}")

                try:
                    idx_al = int(input("Escolha o aluno: ")) - 1
                    if 0 <= idx_al < len(alunos):
                        data_criacao = input(
                            "Data de Criação da Ficha (DD/MM/AAAA): "
                        )
                        objetivo = input("Objetivo do Treino: ")
                        ficha = FichaDeTreino(data_criacao, objetivo)

                        while True:
                            add_ex = input(
                                "Deseja adicionar um exercício à ficha? (s/n): "
                            ).lower()
                            if add_ex == "s":
                                ex_nome = input("Nome do Exercício: ")
                                ex_series = int(input("Número de Séries: "))
                                ex_reps = int(input("Número de Repetições: "))
                                ficha.addExercicio(ex_nome, ex_series, ex_reps)
                                print("Exercício adicionado à ficha!")
                            else:
                                break

                        instrutor_atual.atualizarFicha(alunos[idx_al], ficha)
                        print(
                            "Ficha de treino vinculada ao aluno com sucesso!"
                        )
                    else:
                        print("Aluno inválido!")
                except ValueError:
                    print("Entrada inválida!")

            elif op_inst == "0":
                break
            else:
                print("Opção inválida!")

    elif opcao == "3":
        if not alunos:
            print(
                "\nNenhum aluno cadastrado. Solicite ao atendente o cadastro prévio."
            )
            continue

        print("\n--- SELECIONE O ALUNO ---")
        for idx, al in enumerate(alunos):
            print(
                f"{idx + 1}. {al.get_info('nome')} (Matrícula: {al.get_info('matricula')})"
            )

        try:
            escolha = int(input("Escolha seu perfil: ")) - 1
            if escolha < 0 or escolha >= len(alunos):
                print("Aluno não encontrado!")
                continue
            aluno_atual = alunos[escolha]
        except ValueError:
            print("Entrada inválida!")
            continue

        while True:
            menu_aluno()
            op_al = input("Escolha uma opção: ")

            if op_al == "1":
                print(f"\n{aluno_atual}")
                print(f"Status do Plano: {aluno_atual.get_info('status')}")
                print(f"Nota/Avaliação: {aluno_atual.get_info('nota')}")

            elif op_al == "2":
                idade = aluno_atual.calcularIdade()
                print(f"\nIdade do Aluno: {idade} anos")

            elif op_al == "3":
                ficha = aluno_atual.consultarFicha()
                if isinstance(ficha, FichaDeTreino):
                    print("\n--- EXERCÍCIOS DA FICHA ---")
                    ficha.listarExercicios()
                    print(f"Duração Estimada: {ficha.calcularDuracao()}")
                else:
                    print(f"\nFicha: {ficha}")

            elif op_al == "4":
                print("\nOpções de Plano: 0 - Básico | 1 - Médio | 2 - Avançado")
                try:
                    tp = int(input("Escolha o novo plano (0, 1 ou 2): "))
                    if tp in [0, 1, 2]:
                        aluno_atual.alterarPlano(tp)
                        print(
                            f"Plano alterado para: {aluno_atual.get_info('plano')}"
                        )
                    else:
                        print("Opção inválida!")
                except ValueError:
                    print("Entrada inválida!")

            elif op_al == "5":
                aluno_atual.ativarPlano()
                print("Plano ativado com sucesso!")

            elif op_al == "6":
                aluno_atual.cancelarPlano()
                print("Plano cancelado/desativado com sucesso!")

            elif op_al == "0":
                break
            else:
                print("Opção inválida!")

    elif opcao == "0":
        print("\nEncerrando o sistema da academia. Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.")