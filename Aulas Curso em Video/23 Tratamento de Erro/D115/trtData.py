def appData():
    name = input("Digite o nome: ")
    while True:
        try:
            idade = int(input("Digite a idade: "))
        except ValueError:
            print("Digite um valor inteiro pra a idade.")
        else:
            break


appData()
