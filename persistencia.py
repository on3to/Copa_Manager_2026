import os

def salvar_selecoes(selecoes):
    with open("selecoes.txt", "w", encoding="utf-8") as arquivo:
        for selecao in selecoes:
            linha = f'{selecao["id"]};{selecao["nome"]};{selecao["confederacao"]};{selecao["grupo"]};{selecao["ranking_FIFA"]};{selecao["titulos"]}\n'
            arquivo.write(linha)

    print("Seleções salvas com sucesso!")
    
def carregar_selecoes():
    selecoes = []

    if not os.path.exists("selecoes.txt"):
        return selecoes

    with open("selecoes.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")

            selecao = {
                "id": int(dados[0]),
                "nome": dados[1],
                "confederacao": dados[2],
                "grupo": dados[3],
                "ranking_FIFA": int(dados[4]),
                "titulos": int(dados[5])
            }

            selecoes.append(selecao)

    return selecoes

def salvar_jogadores(jogadores):

    with open("jogadores.txt", "w", encoding="utf-8") as arquivo:

        for jogador in jogadores:

            linha = (
                f'{jogador["id"]};'
                f'{jogador["nome"]};'
                f'{jogador["idade"]};'
                f'{jogador["posicao"]};'
                f'{jogador["camisa"]};'
                f'{jogador["gols"]};'
                f'{jogador["selecao_id"]}\n'
            )

            arquivo.write(linha)

    print("Jogadores salvos com sucesso!")

def carregar_jogadores():

    jogadores = []

    if not os.path.exists("jogadores.txt"):
        return jogadores

    with open("jogadores.txt", "r", encoding="utf-8") as arquivo:

        for linha in arquivo:

            dados = linha.strip().split(";")

            jogador = {
                "id": int(dados[0]),
                "nome": dados[1],
                "idade": int(dados[2]),
                "posicao": dados[3],
                "camisa": int(dados[4]),
                "gols": int(dados[5]),
                "selecao_id": int(dados[6])
            }

            jogadores.append(jogador)

    return jogadores    

def salvar_partidas(partidas):

    with open("partidas.txt", "w", encoding="utf-8") as arquivo:

        for partida in partidas:

            linha = (
                f'{partida["id"]};'
                f'{partida["mandante"]};'
                f'{partida["visitante"]};'
                f'{partida["gols_mandante"]};'
                f'{partida["gols_visitante"]}\n'
            )

            arquivo.write(linha)

    print("Partidas salvas com sucesso!")

def carregar_partidas():

    partidas = []

    if not os.path.exists("partidas.txt"):
        return partidas

    with open("partidas.txt", "r", encoding="utf-8") as arquivo:

        for linha in arquivo:

            dados = linha.strip().split(";")

            partida = {
                "id": int(dados[0]),
                "mandante": int(dados[1]),
                "visitante": int(dados[2]),
                "gols_mandante": int(dados[3]),
                "gols_visitante": int(dados[4])
            }

            partidas.append(partida)

    return partidas