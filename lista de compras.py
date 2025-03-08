arquivo = "listaDeCompras.txt"

def adicionarItem():
    item = input("digite o item para adicionar a lista")

    with open(arquivo, "a") as arq:
        arq.write(item + "\n")
    print(f"{item} adicionado à lista!")

def visualizarlista():
    try:
        with open(arquivo, "r") as arq:
            itens = arq.readlines()
            if not itens:
                print("A Lista esta vazia")
            else:
                print("lista de compras: ")
                for i, item in enumerate(itens, start =1):
                    print(i, item.strip())
    except FileNotFoundError:
        print("A lista não existe!")

def removeritem():
    visualizarlista()
    try:
        num = int(input("digite o numero do item para remover")) -1
        with open(arquivo, "r") as arq:
            itens = arquivo.readllines()
        if 0 < num < len(itens):
            itemRemovido = itens.pop(num)
            with open(arquivo, "w") as arq:
                arq.writelines(itens)
            print(f"{itemRemovido.strip()}foi removido")
        else:
            print("o item não existe!")
    except(ValueError, FileNotFoundError):
        print("falha ao remover item do sistema") 
while True: 
    print("SUA LISTA DE COMPRAS✔.COM.BR") 
    print("1 - ADICIONE ITENS")
    print("2 - VISUALIZAR LISTA")          
    print("3 - REMOVER ITEM")
    print("4 - SAIR")
    opcao = int(input("digite uma opcao: "))

    if opcao == 1:
        adicionarItem()
    elif opcao == 2:
        visualizarlista()
    elif opcao == 3:
        removeritem()
    elif opcao == 4:
        print("saindo...")
        break   
    else:
        print("opção invalida")
