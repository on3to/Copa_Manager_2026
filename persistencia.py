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