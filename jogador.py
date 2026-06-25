from utils import gerar_id, sucesso

def cadastrar_jogador(selecoes, jogadores):

    if len(selecoes) == 0:
        print("Nenhuma seleção cadastrada.")
        return

    print("\n=== Seleções Cadastradas ===")

    for selecao in selecoes:
        print(f'ID: {selecao["id"]} - {selecao["nome"]}')

    selecao_id = int(input("\nDigite o ID da seleção: "))

    selecao_encontrada = False

    for selecao in selecoes:
        if selecao["id"] == selecao_id:
            selecao_encontrada = True
            break

    if not selecao_encontrada:
        print("ID da seleção inválido.")
        return

    proximo_id = gerar_id(jogadores)

    nome = input("Nome do jogador: ")
    idade = int(input("Idade: "))
    posicao = input("Posição: ")
    camisa = int(input("Número da camisa: "))
    gols = int(input("Quantidade de gols: "))

    novo_jogador = {
        "id": proximo_id,
        "nome": nome,
        "idade": idade,
        "posicao": posicao,
        "camisa": camisa,
        "gols": gols,
        "selecao_id": selecao_id
    }

    jogadores.append(novo_jogador)

    sucesso()

def lista_jogador(selecoes, jogadores):

    menu = '''
    |>>> Jogadores <<<|
    1 - Listar
    2 - Ordenar
    ----------------
    0 - Sair >>
    '''

    opcao = int(input(menu))

    while opcao != 0:

        if opcao == 1:

            if len(jogadores) == 0:
                print("Nenhum jogador cadastrado")

            else:

                for jogador in jogadores:

                    nome_selecao = "Não encontrada"

                    for selecao in selecoes:
                        if selecao["id"] == jogador["selecao_id"]:
                            nome_selecao = selecao["nome"]
                            break

                    print("ID:", jogador["id"])
                    print("Nome:", jogador["nome"])
                    print("Idade:", jogador["idade"])
                    print("Posição:", jogador["posicao"])
                    print("Camisa:", jogador["camisa"])
                    print("Gols:", jogador["gols"])
                    print("Seleção:", nome_selecao)
                    print("-" * 20)

        elif opcao == 2:

            menu = '''
            |>>> Ordenar <<<|

            Ordenar por:

            1 - Nome
            2 - Idade
            3 - Gols

            ----------------
            0 - Sair >>
            '''

            opcao = int(input(menu))

            if opcao == 1:
                atributo = "nome"

            elif opcao == 2:
                atributo = "idade"

            elif opcao == 3:
                atributo = "gols"

            else:
                print("Opção inválida")
                return

            menu_ordem = '''
            |>>> Ordem <<<|

            1 - Crescente
            2 - Decrescente

            ----------------
            '''

            opcao_ordem = int(input(menu_ordem))

            if opcao_ordem == 1:
                reverse = False

            elif opcao_ordem == 2:
                reverse = True

            else:
                print("Opção inválida")
                return

            jogadores_ordenados = sorted(
                jogadores,
                key=lambda jogador: jogador[atributo],
                reverse=reverse
            )

            for jogador in jogadores_ordenados:

                nome_selecao = "Não encontrada"

                for selecao in selecoes:
                    if selecao["id"] == jogador["selecao_id"]:
                        nome_selecao = selecao["nome"]
                        break

                print("ID:", jogador["id"])
                print("Nome:", jogador["nome"])
                print("Idade:", jogador["idade"])
                print("Posição:", jogador["posicao"])
                print("Camisa:", jogador["camisa"])
                print("Gols:", jogador["gols"])
                print("Seleção:", nome_selecao)
                print("-" * 20)

        opcao = int(input(menu))

def filtrar_jogador(selecoes, jogadores):

    menu = '''
    |>>> Filtrar Jogadores <<<|
    1 - Filtrar por seleção
    2 - Filtrar por posição
    ----------------
    0 - Voltar >>
    '''

    opcao = int(input(menu))

    while opcao != 0:

        if opcao == 1:

            if len(selecoes) == 0:
                print("Nenhuma seleção cadastrada.")

            elif len(jogadores) == 0:
                print("Nenhum jogador cadastrado.")

            else:

                print("\n=== Seleções Cadastradas ===")

                for selecao in selecoes:
                    print(f'ID: {selecao["id"]} - {selecao["nome"]}')

                id_busca = int(input("\nDigite o ID da seleção: "))

                encontrou = False

                for jogador in jogadores:

                    if jogador["selecao_id"] == id_busca:

                        print("ID:", jogador["id"])
                        print("Nome:", jogador["nome"])
                        print("Idade:", jogador["idade"])
                        print("Posição:", jogador["posicao"])
                        print("Camisa:", jogador["camisa"])
                        print("Gols:", jogador["gols"])
                        print("-" * 20)

                        encontrou = True

                if not encontrou:
                    print("Nenhum jogador encontrado para essa seleção.")

        elif opcao == 2:

            if len(jogadores) == 0:
                print("Nenhum jogador cadastrado.")

            else:

                posicao = input("Digite a posição: ").lower()

                encontrou = False

                for jogador in jogadores:

                    if jogador["posicao"].lower() == posicao:

                        nome_selecao = ""

                        for selecao in selecoes:
                            if selecao["id"] == jogador["selecao_id"]:
                                nome_selecao = selecao["nome"]
                                break

                        print("ID:", jogador["id"])
                        print("Nome:", jogador["nome"])
                        print("Idade:", jogador["idade"])
                        print("Posição:", jogador["posicao"])
                        print("Camisa:", jogador["camisa"])
                        print("Gols:", jogador["gols"])
                        print("Seleção:", nome_selecao)
                        print("-" * 20)

                        encontrou = True

                if not encontrou:
                    print("Nenhum jogador encontrado.")

        else:
            print("Opção inválida.")

        opcao = int(input(menu))

def estatisticas_jogadores(jogadores):

    if len(jogadores) == 0:
        print("Nenhum jogador cadastrado.")
        return

    menu = '''
    |>>> Estatísticas <<<|
    1 - Artilheiro
    2 - Média de idade
    3 - Total de gols
    ----------------
    0 - Voltar >>
    '''

    opcao = int(input(menu))

    while opcao != 0:

        if opcao == 1:

            artilheiro = jogadores[0]

            for jogador in jogadores:
                if jogador["gols"] > artilheiro["gols"]:
                    artilheiro = jogador

            print("Artilheiro")
            print("Nome:", artilheiro["nome"])
            print("Gols:", artilheiro["gols"])

        elif opcao == 2:

            soma_idades = 0

            for jogador in jogadores:
                soma_idades += jogador["idade"]

            media = soma_idades / len(jogadores)

            print(f"Média de idade: {media:.2f}")

        elif opcao == 3:

            total_gols = 0

            for jogador in jogadores:
                total_gols += jogador["gols"]

            print("Total de gols:", total_gols)

        else:
            print("Opção inválida.")

        opcao = int(input(menu))      
        
         