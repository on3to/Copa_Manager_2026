from utils import gerar_id, sucesso

def cadastrar_seleção(selecoes):
    proximo_id = gerar_id(selecoes)   

    nome: str = input("Nome: ")
    confederacao = input("Confederação: ")
    grupo = input("Grupo: ")
    ranking = int(input("Ranking FIFA: "))
    titulos = int(input("Títulos: "))
            

    nova_selecao = {
        "id": proximo_id,
        "nome": nome,
        "confederacao": confederacao,
        "grupo": grupo,
        "ranking_FIFA": ranking,
        "titulos": titulos
            }
    selecoes.append(nova_selecao)
    print(selecoes)
    sucesso()

def lista_selecao(selecoes):

    menu = '''
    |>>> filtrar <<<|
    1 - Listar
    2 - Ordenar
    ----------------
    0 - sair >> '''
    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1: 
            imprimir_selecoes(selecoes)
        elif opcao == 2:
                ordenar_selecao(selecoes)
        opcao = int(input(menu))        

def imprimir_selecoes(selecoes):
    if len(selecoes) == 0:
        print("Nenhuma seleção cadastrada")
    else:
        for nova_selecao in selecoes:
            print("ID:", nova_selecao["id"])
            print("Nome:", nova_selecao["nome"])
            print("Confederação:", nova_selecao["confederacao"])    
            print("Grupo:", nova_selecao["grupo"])    
            print("ranking_FIFA:", nova_selecao["ranking_FIFA"])    
            print("Titulos:", nova_selecao["titulos"])  
            print("-" * 20) 
                                     
def buscar_nome(selecoes):
        nome_buscar = input("Qual seleção deseja buscar:").lower()
        encontrou = False

        for selecao in selecoes:
            if nome_buscar in selecao["nome"].lower():
                  print(selecao["nome"])
                  encontrou = True  
        if encontrou == False:
            print("seleção não encontrada")   
        sucesso()      

def filtrar_grupo_e_conf(selecoes):
    menu = '''
    |>>> filtrar <<<|
    1 - filtrar grupo
    2 - filtrar confederação
    ----------------
    0 - sair >> '''
    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1:
            grupo_buscar = input("Digite o grupo:").upper()
            encontrou = False

            for selecao in selecoes:
                if grupo_buscar == selecao["grupo"].upper():
                        print("Nome:", selecao["nome"])
                        print("Grupo:", selecao["grupo"])
                        print("-" * 20)
                        encontrou = True
            if encontrou == False:
                print("Grupo não encontrado") 

        elif opcao == 2:
            conf_buscar = input("Digite a confederação:").upper()        
            encontrou = False
            
            for selecao in selecoes:
                if conf_buscar == selecao["confederacao"].upper():
                     print("Nome:", selecao["nome"])
                     print("Confederação:", selecao["confederacao"])
                     print("-" * 20)
                     encontrou = True
            if encontrou == False:
                 print("Confederação não encontrada")
        opcao = int(input(menu))            

def ordenar_selecao(selecoes):

    menu = '''
    |>>> Ordenar <<<|
    Ordenar por qual atributo?
    1 - Nome
    2 - Ranking FIFA
    3 - Títulos

    ----------------
    0 - sair >> '''
    opcao = int(input(menu))

    if opcao == 1:
        atributo = "nome"

    elif opcao == 2:
        atributo = "ranking_FIFA"

    elif opcao == 3:
        atributo = "titulos"
    
    else:
        print("Opção ivalida")
        return   

    menu_ordem = '''
    |>>> Ordem <<<|
    Ordenar em qual ordem?
    1 - crescente
    2 - Decrescente

    ----------------
     ''' 
    opcao_ordem = int(input(menu_ordem))
    reverse = False

    if opcao_ordem == 1:
        reverse = False

    elif opcao_ordem == 2: 
        reverse = True   

    else:
        print("Opção invalida")
        return    

    selecoes_ordenadas = sorted(selecoes, key=lambda selecao:selecao[atributo], reverse=reverse)    
    imprimir_selecoes(selecoes_ordenadas)
