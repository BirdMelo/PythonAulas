# Crie um pequeno sistema modularizado que permite
#   cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema vai ter só duas opções: Cadastrar uma nova pessoa e
#   listar todas as pessoas cadastradas.
while True:
    try:
        print("1 - Ver a lista de pessoas.")
        print("2 - Adicionar uma pessoa.")
        print("3 - Sair do programa.")
        option = int(input(""))
        if option > 3 or option < 1:
            print("Essa opção é inexistente.")
    except ValueError:
        print("Por favor, digite um número que representa uma das opções.")
    else:
        if option == 1:
            print("desenvolvimento_1")
        elif option == 2:
            print("desenvolvimento_2")
        else:
            print("desenvolvimento_3")
