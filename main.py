import os

from selecao import cadastrar_seleção, lista_selecao, buscar_nome, filtrar_grupo_e_conf, ordenar_selecao
from persistencia import salvar_selecoes, carregar_selecoes


def main():
    
    menu = '''
    --- SELEÇÕES ---
    1 - cadastrar seleção
    2 - listar/ordenar seleção
    3 - buscar seleção por nome
    4 - filtrar por grupo ou confederação
    
    ---JOGADOES---
    5. Cadastrar jogador (vinculado a uma selecao)
    6. Listar / ordenar jogadores
    7. Filtrar jogadores
    8. Artilheiros e estatisticas (media de idade, total de gols)

    --- PARTIDAS ---
    9. Cadastrar partida
    10. Listar partidas
    11. Tabela de classificacao por grupo
    
    --- SISTEMA ---
    12. Salvar dados em arquivo
    0. Sair (salva automaticamente)

    ----------------
    0 - sair >> '''

    opcao = int(input(menu))
    selecoes = carregar_selecoes()

    while opcao != 0: 
        if opcao == 1:
            cadastrar_seleção(selecoes)

        elif opcao == 2:
            lista_selecao(selecoes)


        elif opcao == 3:
            buscar_nome(selecoes)    

        elif opcao == 4:
            filtrar_grupo_e_conf(selecoes)

        elif opcao == 12:
            salvar_selecoes(selecoes)

        opcao = int(input(menu))

    salvar_selecoes(selecoes)
    print("Dados salvos com sucesso!")    

main()          
