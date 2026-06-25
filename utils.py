def gerar_id(selecoes):
    if len(selecoes) == 0:
        return 1

    return selecoes[-1]["id"] + 1

def sucesso():
    print("operação concluida")

