import os

from selecao import cadastrar_seleção, lista_selecao, buscar_nome, filtrar_grupo_e_conf, ordenar_selecao
from persistencia import salvar_selecoes,carregar_selecoes,salvar_jogadores,carregar_jogadores,salvar_partidas,carregar_partidas
from jogador import cadastrar_jogador, lista_jogador, filtrar_jogador, estatisticas_jogadores
from partidas import cadastrar_partida, listar_partidas, tabela_classificacao


def menu_principal(selecoes, jogadores, partidas):
    return f'''
    ================================================
    {len(selecoes)} seleções | {len(jogadores)} jogadores | {len(partidas)} partidas
    ================================================

    --- SELEÇÕES ---
    1 - Cadastrar seleção
    2 - Listar / Ordenar seleção
    3 - Buscar seleção por nome
    4 - Filtrar por grupo ou confederação

    --- JOGADORES ---
    5 - Cadastrar jogador (vinculado a uma seleção)
    6 - Listar / Ordenar jogadores
    7 - Filtrar jogadores
    8 - Artilheiros e estatísticas (média de idade, total de gols)

    --- PARTIDAS ---
    9 - Cadastrar partida
    10 - Listar partidas
    11 - Tabela de classificação por grupo

    --- SISTEMA ---
    12 - Salvar dados em arquivo
    0 - Sair (salva automaticamente)

    ----------------
    0 - sair >> '''


def main():

    selecoes = carregar_selecoes()
    jogadores = carregar_jogadores()
    partidas = carregar_partidas()

    opcao = int(input(menu_principal(selecoes, jogadores, partidas)))

    while opcao != 0:

        if opcao == 1:
            cadastrar_seleção(selecoes)

        elif opcao == 2:
            lista_selecao(selecoes)

        elif opcao == 3:
            buscar_nome(selecoes)

        elif opcao == 4:
            filtrar_grupo_e_conf(selecoes)

        elif opcao == 5:
            cadastrar_jogador(selecoes, jogadores)

        elif opcao == 6:
            lista_jogador(selecoes, jogadores)

        elif opcao == 7:
            filtrar_jogador(selecoes, jogadores)

        elif opcao == 8:
            estatisticas_jogadores(jogadores)

        elif opcao == 9:
            cadastrar_partida(selecoes, partidas)

        elif opcao == 10:
            listar_partidas(selecoes, partidas)

        elif opcao == 11:
            tabela_classificacao(selecoes, partidas)

        elif opcao == 12:
            salvar_selecoes(selecoes)
            salvar_jogadores(jogadores)
            salvar_partidas(partidas)
            print("Dados salvos com sucesso!")

        else:
            print("Opção inválida!")

        opcao = int(input(menu_principal(selecoes, jogadores, partidas)))

    salvar_selecoes(selecoes)
    salvar_jogadores(jogadores)
    salvar_partidas(partidas)

    print("Dados salvos com sucesso!")


main()
