from utils import gerar_id, sucesso

def cadastrar_partida(selecoes, partidas):

    if len(selecoes) < 2:
        print("É necessário cadastrar pelo menos duas seleções.")
        return

    print("\n=== Seleções Cadastradas ===")

    for selecao in selecoes:
        print(f'ID: {selecao["id"]} - {selecao["nome"]}')

    mandante = int(input("\nID da Seleção Mandante: "))
    visitante = int(input("ID da Seleção Visitante: "))

    if mandante == visitante:
        print("Uma seleção não pode jogar contra ela mesma.")
        return

    mandante_existe = False
    visitante_existe = False

    for selecao in selecoes:
        if selecao["id"] == mandante:
            mandante_existe = True

        if selecao["id"] == visitante:
            visitante_existe = True

    if not mandante_existe or not visitante_existe:
        print("Uma ou ambas as seleções não existem.")
        return

    gols_mandante = int(input("Gols da seleção mandante: "))
    gols_visitante = int(input("Gols da seleção visitante: "))

    proximo_id = gerar_id(partidas)

    nova_partida = {
        "id": proximo_id,
        "mandante": mandante,
        "visitante": visitante,
        "gols_mandante": gols_mandante,
        "gols_visitante": gols_visitante
    }

    partidas.append(nova_partida)

    sucesso()

def listar_partidas(selecoes, partidas):

    if len(partidas) == 0:
        print("Nenhuma partida cadastrada.")
        return

    for partida in partidas:

        mandante = ""
        visitante = ""

        for selecao in selecoes:

            if selecao["id"] == partida["mandante"]:
                mandante = selecao["nome"]

            if selecao["id"] == partida["visitante"]:
                visitante = selecao["nome"]

        print("ID:", partida["id"])
        print(f'{mandante} {partida["gols_mandante"]} x {partida["gols_visitante"]} {visitante}')
        print("-" * 20)

def tabela_classificacao(selecoes, partidas):

    if len(partidas) == 0:
        print("Nenhuma partida cadastrada.")
        return

    grupo = input("Digite o grupo: ").upper()

    tabela = []

    for selecao in selecoes:

        if selecao["grupo"].upper() == grupo:

            registro = {
                "nome": selecao["nome"],
                "pontos": 0,
                "vitorias": 0,
                "empates": 0,
                "derrotas": 0,
                "gp": 0,
                "gc": 0,
                "saldo": 0
            }

            tabela.append(registro)

    for partida in partidas:

        for registro in tabela:

            selecao_nome = registro["nome"]

            selecao_id = 0

            for selecao in selecoes:
                if selecao["nome"] == selecao_nome:
                    selecao_id = selecao["id"]
                    break

            if selecao_id == partida["mandante"]:

                registro["gp"] += partida["gols_mandante"]
                registro["gc"] += partida["gols_visitante"]

                if partida["gols_mandante"] > partida["gols_visitante"]:
                    registro["vitorias"] += 1
                    registro["pontos"] += 3

                elif partida["gols_mandante"] == partida["gols_visitante"]:
                    registro["empates"] += 1
                    registro["pontos"] += 1

                else:
                    registro["derrotas"] += 1

            elif selecao_id == partida["visitante"]:

                registro["gp"] += partida["gols_visitante"]
                registro["gc"] += partida["gols_mandante"]

                if partida["gols_visitante"] > partida["gols_mandante"]:
                    registro["vitorias"] += 1
                    registro["pontos"] += 3

                elif partida["gols_visitante"] == partida["gols_mandante"]:
                    registro["empates"] += 1
                    registro["pontos"] += 1

                else:
                    registro["derrotas"] += 1

    for registro in tabela:
        registro["saldo"] = registro["gp"] - registro["gc"]

    tabela = sorted(
        tabela,
        key=lambda time: (
            time["pontos"],
            time["saldo"],
            time["gp"]
        ),
        reverse=True
    )

    print("\n=== CLASSIFICAÇÃO ===")

    posicao = 1

    for registro in tabela:

        print(
            posicao,
            "-",
            registro["nome"],
            "| P:",
            registro["pontos"],
            "| V:",
            registro["vitorias"],
            "| E:",
            registro["empates"],
            "| D:",
            registro["derrotas"],
            "| GP:",
            registro["gp"],
            "| GC:",
            registro["gc"],
            "| SG:",
            registro["saldo"]
        )

        posicao += 1