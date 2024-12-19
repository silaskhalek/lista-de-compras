def exibir_menu():
    print("\nLista de Compras")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Mostrar lista")
    print("4. Sair")
    return input("Escolha uma opção: ")

def adicionar_item(lista):
    item = input("Digite o nome do item: ")
    lista.append(item)
    print(f"'{item}' foi adicionado à lista.")

def remover_item(lista):
    item = input("Digite o nome do item para remover: ")
    if item in lista:
        lista.remove(item)
        print(f"'{item}' foi removido da lista.")
    else:
        print(f"'{item}' não está na lista.")

def mostrar_lista(lista):
    if lista:
        print("\nItens na lista:")
        for i, item in enumerate(lista, start=1):
            print(f"{i}. {item}")
    else:
        print("A lista está vazia.")

def main():
    lista = []
    while True:
        opcao = exibir_menu()
        if opcao == "1":
            adicionar_item(lista)
        elif opcao == "2":
            remover_item(lista)
        elif opcao == "3":
            mostrar_lista(lista)
        elif opcao == "4":
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
