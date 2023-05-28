# Crie um programa onde o usuário possa digitar vários valores
#   númericos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados,
#   em ordem crescente.
cont = 1
l: list = []
while True:
    n = int(input(f"Digite o {cont}° número: "))
    if n not in l:
        l.append(n)
        cont += 1
        print(f"Número {n} adicionado com sucesso.")
    else:
        print(f"Número {n} já está registrado.")
    more = " "
    while more not in "sn":
        more = str(input("Deseja continuar? [ S ] [ N ]\n").strip().lower()[0])
        if more not in "sn":
            print("Digitação incorreta. Por favor, confirme corretamente.")
    if more in "n":
        break
print(sorted(l))
